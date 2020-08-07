from django import forms

from .models import Assignment


class BookForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('title', 'author', 'pdf')
