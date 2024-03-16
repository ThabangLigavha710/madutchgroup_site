from django.urls import path
from . import views

urlpatterns = [
    path("", views.subsidiary, name='madutch-subsidiary'),
    path("property", views.property_development, name='madutch-property'),
    path("consulting", views.consulting, name='madutch-consulting'),
    path("cleaning", views.cleaning, name='madutch-cleaning'),
    path("landscaping", views.landscaping, name='madutch-landscaping'),
    path("manufacturing", views.manufacturing, name='madutch-manufacturing'),
    path("supplies", views.general_supplies, name='madutch-supplies'),
]