from django.shortcuts import render, get_object_or_404
from .models import Listing
from .choices import state_choices, bedroom_choices, price_choices
from django.http import HttpResponse

def aboutcpa(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context ={
        'listing':listing
    }
    return render(request, 'listings/aboutcpa.html', context)

def index(request):
    listings = Listing.objects.order_by('-list_date')
    context = {
        'listings':listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context ={
        'listing':listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.all().order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list =  queryset_list.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list=queryset_list.filter(price__lte=price)

    context = {
        'listings': queryset_list,
        'values':request.GET,
        'state_choices':state_choices,
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
    }
    return render(request, 'listings/search.html', context)

