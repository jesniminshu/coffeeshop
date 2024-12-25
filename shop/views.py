from django.shortcuts import render,get_object_or_404
from . models import *
from .models import Category, MenuItem
from .forms import ContactForm

# Create your views here.
def home_view(request):
    categories = Category.objects.all()
    return render(request,'index.html',{"categories":categories})

def about(request):
    
    return render(request,'about.html')




def menu_view(request, category_slug=None):
    categories = Category.objects.all()  
    selected_category = None
    items = MenuItem.objects.all() 

    if category_slug:  
        selected_category = get_object_or_404(Category, slug=category_slug)
        items = MenuItem.objects.filter(category=selected_category)

    return render(request, "menu.html", {"categories": categories,"selected_category": selected_category,
        "items": items,})
    
    return render(request,'menu.html')

def menu_detail(request, item_id):
    
    item = get_object_or_404(MenuItem, pk=item_id)
    
    return render(request, 'menudetail.html', {'item': item})
    
def contact_view(request):
    success_message = None  # Initialize success message variable

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save form data to the database
            success_message = "Your message has been submitted. We will get back to you within 24-48 hours."  
            form = None  # Clear the form after successful submission
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form, 'success_message': success_message})
    