from django.contrib import admin
from .models import Book, Author, BookAuthor, BookReview


# Register your models here.

# admin.site.register([Author, BookAuthor, BookReview])


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'isbn')
    # list_filter = ('title',)
    list_display = ('title', 'isbn')


admin.site.register(Book, BookAdmin)