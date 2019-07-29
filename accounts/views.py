from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are now logged out.")
        return redirect('index')

    return render(request, 'accounts/logout.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in.")

            user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
            myid = request.user.id
            context = {
                'contacts':user_contacts
            }
            return render(request, 'accounts/dashboard.html', context)
        else:
            messages.error(request, "Invalid credentials")
            return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.error(request, "Passwords do not match!")
            return redirect(request, 'register')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect(request, 'register')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect(request, 'register')
            
        user = User.objects.create_user(username=username,first_name=first_name, last_name=last_name, email=email, password=password)
        user.save()
        messages.success(request, "Registered successfully. You can now log in.")
        return redirect('login')
    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    
    contact_count = Contact.objects.count()

    context = {
        'contacts':user_contacts,
        'count': contact_count
    }
    
    return render(request, 'accounts/dashboard.html', context)