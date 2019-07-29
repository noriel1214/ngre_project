from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == "POST":
        user_id = request.POST["user_id"]
        listing_id = request.POST["listing_id"]
        address = request.POST["address"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(user_id=user_id, listing_id=listing_id) 
            if has_contacted:
                messages.error(request, "You have already inquired about this property.")   
                return redirect('/listings/'+listing_id)
            
        contact = Contact(user_id=user_id, listing_id=listing_id,
        address=address, name=name, email=email, phone=phone, message=message)
        contact.save()
        messages.success(request, "Your inquiry has been submitted. Someone will get back to you soon.")
        return redirect('/listings/'+listing_id)