from django.shortcuts import render
from app.models import Book
# Create your views here.


def start_project(request):
    # get принимает одно объект

    # SELECT * FROM book
    # data = Book.objects.all()

    # SELECT * FROM book WHERE pages > 500
    # gt (больше чем)
    # lt (меньше чем)
    # data = Book.objects.filter(pages__gt=500)

    # SELECT * FROM book WHERE pages <= 500
    # data = Book.objects.exclude(pages__gt=500)

    # SELECT * FROM book WHERE pages = 500
    # data = Book.objects.get(id=1)


    # CREATE
    # INSERT INTO book (title, author, pages)
    # VALUES ('NewTitle', 'NewAuthor', 776)
    # 1 способ
    # Book.objects.create(title='NewTitle', author='NewAuthor', pages=776)

    # 2 способ
    # book = Book()
    # book.title = 'NewTitle2'
    # book.author = 'NewAuthor2'
    # book.pages = 654
    # book.save()


    # UPDATE
    # UPDATE book SET author = 'New' WHERE pages > 600
    # Book.objects.filter(pages__gt=500).update(author='ChangeAuthor')

    # book = Book.objects.get(pages=239)
    # book.author = 'Old'
    # book.save()


    # DELETE
    # Book.objects.filter(pages__lt=500).delete()

    # book = Book.objects.get(title='F')
    # book.delete()

    # print(data)



    book = Book.objects.all()
    context = {'book_list' : book, 'var1' : 15}
    return render(request, 'index.html', context=context)