from django import forms
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q

# Create your form here
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone')

# Create your CrUD views here.
def create(request):
    
    # if any field is not empty and send is pressed we send data
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }
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