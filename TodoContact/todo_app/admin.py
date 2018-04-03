from django.contrib import admin
from .models import Book, Author,Todo, Contact
# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Todo)
admin.site.register(Contact)
