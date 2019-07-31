from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]

        contact = Contact(firstname=firstname, lastname=lastname,
        email=email, phone=phone, message=message)
        contact.save()
        messages.success(request, "Your inquiry has been submitted. Someone will get back to you soon.")
        return redirect('index')