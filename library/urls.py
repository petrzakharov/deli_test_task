from django.urls import path

from .views import AddBook, BookDetail, Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
    path('books/add/', AddBook.as_view(), name='add_book'),
]
