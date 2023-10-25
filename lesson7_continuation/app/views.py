from django.shortcuts import render
from django.shortcuts import HttpResponse
from app.models import *

# Create your views here.


def book_list_view(request):
    books = Book.objects.all()
    context = {'book': books}

    return render(request, 'book_list.html', context=context)

#  через pk
# def book_detail_view(request, pk):
#     book = Book.objects.get(id=pk)
#     context = {'books': book}
#
#     return render(request, 'book_detail.html', context=context)


# через slug
def book_detail_view(request, book_slug):
    book = Book.objects.get(slug=book_slug)
    context = {'books': book}

    return render(request, 'book_detail.html', context=context)


# def index_view(request):
#     author = Author.objects.get(pk=1)
#     # books = Book.objects.filter(author=author)
#     books = author.book_set.all()
#     # print(books)
#
#     reader = Reader.objects.get(first_name='X')
#     l_books = reader.liked_books.all()
#     # print(l_books)
#
#     book = Book.objects.get(title='ZZ')
#     l_readers = book.reader_set.all()
#     print(l_readers)
#
#     return HttpResponse('test')