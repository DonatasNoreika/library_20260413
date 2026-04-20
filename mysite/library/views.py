from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, reverse
from .models import Book, BookInstance, Author
from django.views import generic
from django.urls import reverse_lazy
from .forms import InstanceCreateUpdateForm

# Create your views here.

def index(request):
    context = {
        'num_books': Book.objects.count(),
        'num_instances': BookInstance.objects.count(),
        'num_authors': Author.objects.count(),
        'num_instances_available': BookInstance.objects.filter(status='a').count(),
    }
    return render(request, template_name="index.html", context=context)

def authors(request):
    context = {
        'authors': Author.objects.all(),
    }
    return render(request, template_name="authors.html", context=context)

def author(request, author_pk):
    context = {
        'author': Author.objects.get(pk=author_pk)
    }
    return render(request, template_name="author.html", context=context)


class BookListView(generic.ListView):
    model = Book
    template_name = "books.html"
    context_object_name = "books"


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "book.html"
    context_object_name = "book"


class MyBookInstanceListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = "my_books.html"
    context_object_name = "instances"

    def get_queryset(self):
        return BookInstance.objects.filter(reader=self.request.user)


class BookInstanceListView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = BookInstance
    template_name = "instances.html"
    context_object_name = "instances"

    def test_func(self):
        return self.request.user.is_staff


class BookInstanceDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = BookInstance
    template_name = "instance.html"
    context_object_name = "instance"

    def test_func(self):
        return self.request.user.is_staff


class BookInstanceCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = BookInstance
    template_name = "instance_form.html"
    # fields = ['book', 'due_back', 'reader', 'status']
    form_class = InstanceCreateUpdateForm
    success_url = reverse_lazy('instances')

    def test_func(self):
        return self.request.user.is_staff


class BookInstanceUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = BookInstance
    template_name = "instance_form.html"
    # fields = ['book', 'due_back', 'reader', 'status']
    form_class = InstanceCreateUpdateForm
    # success_url = reverse_lazy('instances')

    def get_success_url(self):
        return reverse("instance", kwargs={"pk": self.object.pk})

    def test_func(self):
        return self.request.user.is_staff


class BookInstanceDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = BookInstance
    template_name = "instance_delete.html"
    context_object_name = "instance"
    success_url = reverse_lazy('instances')

    def test_func(self):
        return self.request.user.is_staff