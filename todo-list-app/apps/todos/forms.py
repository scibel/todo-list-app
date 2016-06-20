from django import forms

from .models import ToDoItem


class ToDoForm(forms.Form):
    name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter ToDo item', 'class': 'todo-input'})
    )
    description = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter description', 'class': 'todo-input'})
    )
    priority = forms.CharField(
        label='',
        required=True
    )

    class Meta:
        model = ToDoItem
