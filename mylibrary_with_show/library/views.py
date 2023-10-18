from django.shortcuts import render
from library.models import Book, Reader, BookRent, newBook


# Create your views here.
def show_start_page(request):
    # book = Book.objects.all()
    # context = {'book': book}

    return render(request, "index.html")


def show_books_page(request):
    book = Book.objects.all()
    context = {"books": book}

    return render(request, "showBooks.html", context=context)


def show_readers_page(request):
    reader = Reader.objects.all()
    context = {'readers': reader}

    return render(request, 'showReaders.html', context=context)


def show_rents_page(request):
    rent = BookRent.objects.all()
    context = {'rents': rent}

    return render(request, 'showRents.html', context=context)


def show_addbook_page(request):
    books = Book.objects.all()
    context = {"books": books}
    if request.method == "POST":
        book_title = request.POST.get("book_title")
        author_name = request.POST.get("book_author_name")
        author_surname = request.POST.get("book_author_surname")
        genre = request.POST.get("book_genre")
        publication_year = request.POST.get("publication_year")
        page_count = request.POST.get("page_count")
        description = request.POST.get("description")

        Book.objects.create(title=book_title,
                            author_name=author_name,
                            author_surname=author_surname,
                            publication_year=publication_year,
                            page_count=page_count,
                            genre=genre,
                            description=description)

    return render(request, "addBook.html", context=context)


def show_addreader_page(request):
    if request.method == "POST":
        name = request.POST.get("reader_name")
        reader_surname = request.POST.get("reader_surname")
        reader_age = request.POST.get("reader_age")
        reader_address = request.POST.get("reader_address")

        Reader.objects.create(name=name,
                              surname=reader_surname,
                              age=reader_age,
                              address=reader_address)

    return render(request, "addReader.html")


def show_addrent_page(request):
    if request.method == "POST":
        title = request.POST.get("book_title")
        surname = request.POST.get("reader_surname")
        rent_date = request.POST.get("rent_date")
        return_date = request.POST.get("return_date")

        BookRent.objects.create(book_title=title,
                                reader_surname=surname,
                                rent_date=rent_date,
                                return_date=return_date)

    return render(request, "addRent.html")

