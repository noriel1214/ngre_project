from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]

        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        messages.success(request, "Your inquiry has been submitted. Someone will get back to you soon.")
        return redirect('index')