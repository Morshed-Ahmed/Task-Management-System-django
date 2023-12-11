from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        category_form = forms.CategoryFrom(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category')
    else:
        category_form = forms.CategoryFrom()
    return render(request,'categories/add_category.html',{'form':category_form})



