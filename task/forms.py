from django import forms
from .models import Task

class TaskFrom(forms.ModelForm):
    class Meta:
        model = Task
        fields =  '__all__'
        labels={
            'taskTitle':'Task Title',
            'taskDescription':'Task Description',
            'is_completed':'Is Completed',
            'date':'Task Create Date',
            'categories':'Task Categories'
        }
        widgets = {
            'taskTitle': forms.TextInput(attrs={'placeholder': 'Enter Task Title'}),
            'taskDescription': forms.Textarea(attrs={'placeholder': 'Enter Task Description'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'categories': forms.CheckboxSelectMultiple()
        }
        