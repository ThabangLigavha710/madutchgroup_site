from django.urls import path
from . import views

urlpatterns = [
    path("", views.subsidiary, name='madutch-subsidiary'),
    path("property", views.property_development, name='madutch-property'),
    path("consulting", views.consulting, name='madutch-consulting'),
]