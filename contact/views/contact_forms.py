from typing import Any, Dict
from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import ContactForm
from django.urls import reverse
from contact.models import Contact

# Create your CrUD views here.
def create(request):
    
    form_action = reverse('contact:create')
    
    # if any field is not empty and send is pressed we send data
    if request.method == 'POST':
        
        form = ContactForm(request.POST)
        
        context = {
            'form': form,
            'form_action': form_action,
        }
        
        if form.is_valid():
            print('form is valid')
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)
        
        return render(
            request,
            'contact/create.html',
            context,
        )
    
    # if fields are empty we will see the empty form again
    context = {
        'form': ContactForm(),
        'form_action': form_action,
    }
    
    return render(
        request,
        'contact/create.html',
        context,
    )
    
def update(request, contact_id):
    
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    
    form_action = reverse('contact:update', args=(contact_id,))
    
    # if any field is not empty and send is pressed we send data
    if request.method == 'POST':
        
        form = ContactForm(request.POST, instance=contact)
        
        context = {
            'form': form,
            'form_action': form_action,
        }
        
        if form.is_valid():
            print('form is valid')
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)
        
        return render(
            request,
            'contact/create.html',
            context,
        )
    
    # if fields are empty we will see the empty form again
    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }
    
    return render(
        request,
        'contact/create.html',
        context,
    )