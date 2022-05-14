from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=200, null=True)
    pageCount = models.IntegerField(default=0)
    #thumbnailUrl = models.CharField(max_length=200, null=True)
    shortDescription = models.CharField(max_length=200, null=True)
    longDescription = models.TextField(null=True)
    authors = models.ManyToManyField(
        Author)
    image = models.ImageField(upload_to="images", null=True)

    def __str__(self):
        return f"{self.id} - {self.title}"


class Review(models.Model):
    body = models.TextField(null=True)
    #book_id = models.BigIntegerField(null=True)
    # models.BigIntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True, null=True)
    image = models.ImageField(upload_to="images/review", null=True)
