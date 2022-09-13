from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from postgres_setup_app.models import Author, Book
from postgres_setup_app.forms import BookForm, AuthorForm

# -- FUNCTIONAL VIEW
# def book_list(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#     return render(
#         request,
#         'postgres_setup_app/book_list.html',
#         {'books': books}
#     )

# -- CLASS BASED VIEW
# class BookListView(View):
#     def get(self, request):
#         books = Book.objects.all()
#         return render(
#             request,
#             'postgres_setup_app/book_list.html',
#             {'books': books}
#         )

class BookListView(ListView):
    # model = Book
    queryset = Book.objects.order_by('title')
    context_object_name = 'book_list'


# def book_details(request, book_id):
#     if request.method == 'GET':
#         book = Book.objects.get(id=book_id)
#     return render(
#         request,
#         'postgres_setup_app/book_details.html',
#         {'book': book}
#     )

class BookDetailsView(View):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        return render(
            request,
            'postgres_setup_app/book_details.html',
            {'book': book}
        )


class AuthorListView(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(
            request,
            'postgres_setup_app/author_list.html',
            {'authors': authors}
        )

# def author_list(request):
#     authors = Author.objects.all()
#     return render(
#         request,
#         'postgres_setup_app/author_list.html',
#         {'authors': authors}
#     )

class AuthorDetailsView(View):
    def get(self, request, author_id):
        author = Author.objects.get(id=author_id)
        return render(
            request,
            'postgres_setup_app/author_details.html',
            {'author': author}
        )

# def author_details(request, author_id):
#     author = Author.objects.get(id=author_id)
#     return render(
#         request,
#         'postgres_setup_app/author_details.html',
#         {'author': author}
#     )

class BookAddView(View):
    form_class = BookForm
    template_name = 'postgres_setup_app/book_add.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        return render(request, self.template_name, {'form': form})


# def book_add(request):
#     if request.method == "POST":
#         form = BookForm()
#         if form.is_valid():
#             return HttpResponseRedirect('/success/')
#     return render(
#         request,
#         'postgres_setup_app/book_add.html',
#         {'form': form}
#     )

class AuthorAddView(View):
    form_class = AuthorForm
    template_name = 'postgres_setup_app/author_add.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        return render(request, self.template_name, {'form': form})

# def author_add(request):
#     form = AuthorForm()
#     return render(
#         request,
#         'postgres_setup_app/author_add.html',
#         {'form': form}
#     )