from django.urls import path
from .views import ContactListView, ContactCreateView, ContactDetailView, ContactUpdateView, ContactDeleteView

urlpatterns = [
    path('',ContactListView.as_view(), name="contactList"),
    path('addContact/',ContactCreateView.as_view(), name="createContact"),
    path('detail/<int:pk>', ContactDetailView.as_view() ,name="contact_detail"),
    path('edit/<int:pk>', ContactUpdateView.as_view(), name="contact_update"),
    path('delete/<int:pk>', ContactDeleteView.as_view(), name="contact_delete"),
]