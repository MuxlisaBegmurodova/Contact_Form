from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Contact
from .forms import ContactForm

# Create your views here.
class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact_new.html'
    success_url = reverse_lazy('contact_list')

class ContactList(ListView):
    model = Contact
    template_name = 'contact_list.html'