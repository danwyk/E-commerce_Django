from django import forms
from .models import Item
from django.contrib.auth.models import User


INPUT_CLASS = 'w-full px-6 py-4 rounded-xl border-2'


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'name', 'description', 'price', 'image',]
    
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASS
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASS
            }),
            # 'created by': forms.FileInput(attrs={
            #     'class': INPUT_CLASS,
            #     'value': User
            # }),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'image', 'isSold']
    
        widgets = {
            
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASS
            }),
        }