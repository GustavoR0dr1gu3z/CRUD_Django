from django import forms
from.models import Contact # Importamos el script models


class ContactForm(forms.ModelForm): # Importamos modelform de los forms
    class Meta: # Define que modelo trabajará
        model = Contact 
        fields = "__all__" # Llamar a todos los campos ya definidas en la clase 




