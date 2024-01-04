from django.shortcuts import render

# Create your views here.
def subsidiary(request):
    return render(request, "subsidiary/subsidiary.html", {'title': 'Subsidiary'})
