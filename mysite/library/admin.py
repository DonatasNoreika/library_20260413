from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# Register your models here.

class BookInstanceInLine(admin.TabularInline):
    model = BookInstance
    extra = 0

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn']
    inlines = [BookInstanceInLine]

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance)