from django.urls import path
from postgres_setup_app.views import (BookListView, AuthorListView,
    BookDetailView, AuthorDetailView, BookFormView, AuthorFormView,
    AuthorDeleteView)


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('author_list', AuthorListView.as_view(), name='author_list'),
    path('book_detail/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('author_details/<int:pk>', AuthorDetailView.as_view(), name='author_details'),
    path('book_add', BookFormView.as_view(), name='book_add'),
    path('author_add', AuthorFormView.as_view(), name='author_add'),
    path('author_delete/<int:pk>', AuthorDeleteView.as_view(), name='author_delete'),
]