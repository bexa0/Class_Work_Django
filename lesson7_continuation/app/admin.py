from django.contrib import admin
from app.models import Author, Book, Reader, Ticket

# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(Ticket)
