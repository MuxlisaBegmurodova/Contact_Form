from django.urls import path
from .views import ContactView, ContactList

urlpatterns = [
    path('',ContactView.as_view(), name='contact_new'),
    path('xabarlar/', ContactList.as_view(), name='contact_list')
]