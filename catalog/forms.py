from django import forms

from.models import Book


class BookEntryForm(forms.ModelForm):
    model = Book
    fields = ('title', 'isbn')