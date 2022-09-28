from django.contrib import admin

from postgres_setup_app.models import Author, Book, BookClub, ISBN13


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "author_books")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    def get_ordering(self, request):
        if request.user.is_superuser:
            return ['title']


    list_display = ("title", "author")
    search_fields = ['author__name', 'title']
    list_filter = ("author", )


@admin.register(BookClub)
class BookClubAdmin(admin.ModelAdmin):
    list_display = ("name", "members")


@admin.register(ISBN13)
class ISBN13Admin(admin.ModelAdmin):
    list_display = ("value", "book")