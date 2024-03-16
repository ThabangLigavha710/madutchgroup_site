from django.shortcuts import render

# Create your views here.
def subsidiary(request):
    return render(request, "subsidiary/subsidiary.html", {'title': 'Subsidiary'})


def property_development(request):
    return render(request, "subsidiary/property.html", {'title': 'Property Development'})


def consulting(request):
    return render(request, "subsidiary/consulting.html", {'title': 'Consulting'})


def cleaning(request):
    return render(request, "subsidiary/cleaning.html", {'title': 'Cleaning'})


def landscaping(request):
    return render(request, "subsidiary/landscaping.html", {'title': 'Landscaping'})


def manufacturing(request):
    return render(request, "subsidiary/manufacturing.html", {'title': 'Manufacturing'})


def general_supplies(request):
    return render(request, "subsidiary/supplies.html", {'title': 'General Supplies'})
