from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Book, BookInstance, Author
from django.views import generic

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