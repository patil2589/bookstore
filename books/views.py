# from django.http import Http404
from contextlib import redirect_stderr
from email.mime import image
from multiprocessing import context, get_context
from pyexpat import model
from django.forms import ModelForm
from django.shortcuts import get_object_or_404
# from multiprocessing import context
# from pyexpat import model
from django.shortcuts import render, redirect

import books
# import json
from .models import Author, Book, Review
from django.views.generic import ListView, DetailView
# bookData = open("new.json").read()
# data = json.loads(bookData)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from books.forms import ReviewForm


class BookListView(ListView):

    # template_name = "books/index.html"         #index.html->book_list
    # context_object_name = "books"         #book_list

    def get_queryset(self):
        return Book.objects.all()

# def index(request):
#     data = Book.objects.all()
#     books = {'books': data}
#     # print(data)
#     return render(request, "books/index.html", books)


class BookDetailView(DetailView):

    model = Book

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['authors'] = context['book'].authors.all()
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        context['form'] = ReviewForm()
        return context


# def show(request, id):
#     # try:
#     #     singleBook = Book.objects.get(pk=id)
#     # except Book.DoesNotExist:
#     #     raise Http404("Data not found")
#     # for book in data:
#     #     if book['id'] == id:
#     #         singleBook = book
#     singleBook = get_object_or_404(Book, pk=id)
#     reviews = Review.objects.filter(book_id=id).order_by('-created_at')

#     books = {'books': singleBook, 'reviews': reviews}
#     return render(request, "books/show.html", books)


def review(request, id):
    if request.user.is_authenticated:
        # body = request.POST['body']
        # data = Review(body=body, book_id=id,
        #               user=request.user)
        # data.save()
        # image = request.FILES['image']
        # if image.len != 0:
        #     fs = FileSystemStorage()
        #     name = fs.save(image.name, image)
        #     data = Review(image=fs.url(name))
        #     data.save()
        newdata = Review(book_id=id, user=request.user)
        form = ReviewForm(request.POST, request.FILES, instance=newdata)
        if form.is_valid:
            form.save()
        else:
            print("Not valid")
    return redirect('index')


def author(request, author):
    books = Book.objects.filter(authors__name=author)
    context = {'book_list': books}
    return render(request, 'books/book_list.html', context)
