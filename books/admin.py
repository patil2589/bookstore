from pyexpat import model
from sys import modules
from django.contrib import admin
from .models import Author, Book
# Register your models here.


admin.site.register(Book)
admin.site.register(Author)