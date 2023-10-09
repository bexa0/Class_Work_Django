from django.shortcuts import render
from app.models import Book
# Create your views here.


def start_page(request):
    books = Book.objects.all()
    print(books)
    return render(request, 'start.html')


def new_page(request):
    return render(request, 'new.html')
