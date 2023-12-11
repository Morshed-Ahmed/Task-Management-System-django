from django import forms
from .models import Category

class CategoryFrom(forms.ModelForm):
    class Meta:
        model = Category
        fields =  '__all__'
        labels ={
            'name':'Category Name'
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Category Name'}),
        }