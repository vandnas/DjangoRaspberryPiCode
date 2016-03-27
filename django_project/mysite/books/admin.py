from django.contrib import admin

from .models import books


class booksAdmin(admin.ModelAdmin):
    fields = ['book_id', 'book_name','book_author']

admin.site.register(books, booksAdmin)
