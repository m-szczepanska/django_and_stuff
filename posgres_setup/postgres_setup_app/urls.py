from django.urls import path
from postgres_setup_app.views import (BookListView, AuthorListView,
    BookDetailsView, AuthorDetailsView, BookAddView, AuthorAddView)


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('author_list', AuthorListView.as_view(), name='author_list'),
    path('book_details/<int:book_id>/', BookDetailsView.as_view(), name='book_details'),
    path('author_details/<int:author_id>/', AuthorDetailsView.as_view(), name='author_details'),
    path('book_add', BookAddView.as_view(), name='book_add'),
    path('author_add', AuthorAddView.as_view(), name='author_add'),
]