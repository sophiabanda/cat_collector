from django.shortcuts import render
from .models import Cat
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    cats = Cat.objects.all()
    # all gives us all related data
    return render(request, 'cats/index.html', {
        'cats': cats
    })

def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        'cat': cat,
        'feeding_form': feeding_form
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
    
