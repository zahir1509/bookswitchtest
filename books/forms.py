from django import forms
from .models import Book

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'condition', 'phone_number', 'address']
        widgets = {
            'condition': forms.NumberInput(attrs={'type': 'range', 'min': 1, 'max': 5}),
        }