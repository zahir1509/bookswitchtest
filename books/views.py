from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddBookForm

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