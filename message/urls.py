from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='madutch-main'),
    path("contact", views.contact, name='madutch-contact'),
]