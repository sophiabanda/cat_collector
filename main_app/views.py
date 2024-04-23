from django.shortcuts import render
from .models import Cat
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {
        'cats': cats
    })

def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {
        'cat': cat
    })

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    # When the template is rendered for this view it will need to know which fields to add. 
    # This says "when you create this template, add all views"

class CatUpdate(UpdateView):
    model = Cat
    fields = ('name', 'description', 'age')
    # using a tuple for more security and better performance?

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'
    
