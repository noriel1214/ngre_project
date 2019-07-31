from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    context = {
        'listings':listings
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context ={
        'realtors':realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)

def acctsvcs(request):
    return render(request, 'pages/acctsvcs.html')

def taxsvcs(request):
    return render(request, 'pages/taxsvcs.html')

def contactus(request):
    return render(request, 'pages/contactus.html')
