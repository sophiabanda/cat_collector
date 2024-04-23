from django.shortcuts import render, redirect
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

def add_feeding(request, cat_id):
    # access form field input values
    submitted_form = FeedingForm(request.POST) # this creates django's version of req.body
    # validate form input
    if submitted_form.is_valid():
    # if form input is valid, we'll save an in-memory copy of the new feeding object
        new_feeding = submitted_form.save(commit=False)
    # attach the cat id to the in-memory object
        new_feeding.cat_id = cat_id
    # save completed feeding object in the database
        new_feeding.save()
    # redirect back to the cat detail page
    return redirect('detail', cat_id=cat_id)

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
    
