from django.contrib.auth.models import User
from django.db import models
import uuid

# Create your models here.

class Author(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    description = models.TextField(default="")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField()
    summary = models.TextField()
    isbn = models.IntegerField()
    author = models.ForeignKey(to="Author",
                               on_delete=models.SET_NULL,
                               null=True, blank=True,
                               related_name='books')
    genre = models.ManyToManyField(to="Genre")

    def __str__(self):
        return self.title


class BookInstance(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    book = models.ForeignKey(to="Book", on_delete=models.CASCADE, related_name="instances")
    due_back = models.DateField(null=True, blank=True)
    reader = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('d', 'Administered'),
        ('t', 'Taken'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(choices=LOAN_STATUS, default='d')


    def __str__(self):
        return f"{self.book} - {self.uuid}"