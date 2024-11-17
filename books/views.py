from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import AddBookForm
from .models import Book

def home(request):
    return render(request, 'home.html')


def add_books(request):
    if request.method == "POST":
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            # Save form data to the database
            form.save()
            return HttpResponse("Book successfully added!")
    else:
        form = AddBookForm()
    return render(request, 'add_books.html', {'form': form})


def view_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'view_books.html', {'books': books})

def rent_book(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        if not book.is_rented:  # Ensure the book isn't already rented
            book.is_rented = True
            book.save()
            return redirect('books:view_books')  # Redirect back to the book list
    return redirect('books:view_books')

#test comment