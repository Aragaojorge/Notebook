from typing import Any, Dict
from django.shortcuts import render, redirect
from contact.forms import ContactForm

# Create your CrUD views here.
def create(request):
    
    # if any field is not empty and send is pressed we send data
    if request.method == 'POST':
        
        form = ContactForm(request.POST)
        
        context = {
            'form': form
        }
        
        if form.is_valid():
            print('form is valid')
            form.save()
            return redirect('contact:create')
        
        return render(
            request,
            'contact/create.html',
            context,
        )
    
    # if fields are empty we will see the empty form again
    context = {
        'form': ContactForm()
    }
    
    return render(
        request,
        'contact/create.html',
        context,
    )