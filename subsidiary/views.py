from django.shortcuts import render

# Create your views here.
def subsidiary(request):
    return render(request, "subsidiary/subsidiary.html", {'title': 'Subsidiary'})


def property_development(request):
    return render(request, "subsidiary/property.html", {'title': 'Property Development'})


def consulting(request):
    return render(request, "subsidiary/consulting.html", {'title': 'Consulting'})
