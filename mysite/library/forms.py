from .models import BookInstance
from django import forms

class InstanceCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ['book', 'due_back', 'reader', 'status']
        widgets = {'due_back': forms.DateInput(attrs={'type': 'date'})}