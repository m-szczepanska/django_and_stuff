from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % (self.name)

    @property
    def author_books(self):
        return [x['title'] for x in self.book_set.values('title')]


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.title)

    @property
    def author_books(self):
        return [x['title'] for x in self.book_set.values('title')]


class BookClub(models.Model):
    name = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)

    @property
    def members(self):
        return [x['name'] for x in self.authors.values()]

    def __str__(self):
        return "%s" % (self.name)


class ISBN13(models.Model):
    value = models.CharField(max_length=17)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.value)
