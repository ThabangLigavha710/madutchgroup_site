from django.urls import path
from . import views

urlpatterns = [
    path("", views.subsidiary, name='madutch-subsidiary')
]