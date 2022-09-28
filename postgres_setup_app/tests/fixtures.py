from postgres_setup_app.models import Author, Book


def gen_author(name="John Doe"):
    author = Author(name=name)
    author.save()
    return author

def gen_book(title="Best book", author=None):
    book = Book(title=title, author=author)
    book.save()
    return book

