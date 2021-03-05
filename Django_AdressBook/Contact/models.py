from django.db import models
from django.urls import reverse

# Create your models here.
class Contact(models.Model): # Creo clase e importo los modelos
    first_name = models.CharField(max_length=50)    
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True) # Email que acepta nulos
    
    def __str__(self): # Definir metodo con la construccion de la clase Contact
        return f"{self.first_name} {self.last_name}" # Construye una secuencia de caracteres
    
    def get_absolute_url(self):
        return reversed('contact_detail', kwargs={"pk": self.pk})
