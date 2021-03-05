from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DetailView,
    DeleteView,
)
from .models import Contact
from .forms import ContactForm

# Create your views here.


#--------CREANDO LAS VISTAS DE LAS CLASES PARA LA AGENDA--------
class ContactCreateView(CreateView):
    model = Contact

class ContactListView(ListView):
    model = Contact

class ContactDetailView(DetailView):
    model = Contact

class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm

class ContactDeleteView(DeleteView):
    model = Contact
    # success_url = reverse_lazy()

