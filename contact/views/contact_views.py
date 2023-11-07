from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
# Create your views here.
def index(request):
    
    contacts = Contact.objects.filter(show=True).order_by('-id')
    
    # print(contacts.query)
    
    context = {
        'contacts': contacts,
        'site_title': 'Contacts - '
    }
    
    return render(
        request,
        'contact/index.html',
        context,
    )
    
def search(request):
    
    # search_value will receive url
    search_value = request.GET.get('q', '').strip()
    
    contacts = Contact.objects \
    .filter(show=True) \
    .filter(
        Q(first_name__icontains=search_value) |
        Q(last_name__icontains=search_value) |
        Q(phone__icontains=search_value) |
        Q(email__icontains=search_value)
    )\
    .order_by('-id')
    
    # print(contacts.query)
    # print(search_value)
    
    # if search is empty, return to index.html
    if search_value == '':
        return redirect('contact:index')
    
    context = {
        'contacts': contacts,
        'site_title': 'Search - '
    }
    
    return render(
        request,
        'contact/index.html',
        context,
    )
    
# this viwe will show a single contact in template contact.html
# URL will give it a contact_id and this value will be used in the query
def contact(request, contact_id):
    
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    
    # site_title will be used to show the contat name on web page title
    site_title = f'{single_contact.first_name} {single_contact.last_name} - '
    
    context = {
        'contact': single_contact,
        'site_title': site_title,
    }
    
    return render(
        request,
        # it will be rendered the contact.html template
        'contact/contact.html',
        context,
    )