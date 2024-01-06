from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib import messages
from .models import Message
from .forms import SendMassageForm
from django.core.mail import send_mail

# Create your views here.
def home(request):
    form = SendMassageForm()
    context = {
                'form': form,
                'title': 'Home'
            }
    # print(form)
    if request.method == 'POST':
        form = SendMassageForm(request.POST)

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = "New Enquiry from " + email

        email_message = f"""
            Dear Madutch Group,

            Message from customer
            ------------------------------------------------------

            {message}

            Contact Details
            -------------------------------------------------------

            First name: {first_name}
            Last name: {last_name}
            Phone number: {phone_number}
            Email: {email}
        """
        
        if form.is_valid():
            form.save()
            send_mail(subject, email_message, email, ["info@sairelinked.com"])
            return redirect('madutch-main')
        else:
            form = SendMassageForm()

    return render(request, "message/home.html", context);


# def subsidiary(request):
#     return render(request, "message/subsidiary.html", {'title': 'Subsidiary'})