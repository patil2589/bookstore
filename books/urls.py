from django.urls import path
from django.conf.urls.static import static
from . import views
from Bookstore import settings
urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.BookListView.as_view(), name='index'),
    #path('<int:id>/', views.show, name='books.show'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='books.show'),
    path('<int:id>/review', views.review, name='books.review'),
    path('<str:author>', views.author, name='books.author'),
]
