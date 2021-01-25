from django.shortcuts import render
from django.core.paginator import Paginator
import flickrapi
from .models import Preset, FavouritePlaces
from .forms import PresetForm

api_key = "02df6aacd6e20bed557b78d7dc1d143a"
secret_api_key = "5a2087a02ab2540c"
flickr = flickrapi.FlickrAPI(api_key, secret_api_key)





# Search function
def search(lat, lon):
    # Calling Flickr API and Create Photos object
    obj = flickr.photos.search(api_key=api_key, lat=lat, lon=lon, accuracy=11, format='parsed-json')
    photos = obj['photos']['photo']

    # Create photo addresses
    addresses = []
    for photo in photos:
        farm_id = photo['farm']
        server_id = photo['server']
        id = photo['id']
        secret = photo['secret']
        address = f"https://farm{farm_id}.staticflickr.com/{server_id}/{id}_{secret}.jpg"
        addresses.append(address)
    return addresses


def searchByLatAndLon(request):
    presets = Preset.objects.all()
    addresses = ""
    if request.method == 'POST':
        lon = request.POST.get('longitude')
        lat = request.POST.get('latitude')
        addresses = search(lat, lon)

    context = {
        'addresses': addresses,
        "presets": presets,

    }
    return render(request, 'flikcr_api/index.html', context)


# Function that will return urls of input location pictures
def searchCities(request):
    cityid = ""
    addresses = []
    presets = {}
    page = ""

    if request.method == 'POST':
        presets = Preset.objects.all()
        cityname = request.POST.get('city')
        cityid = Preset.objects.get(id=cityname)
        lat = cityid.latitude
        lon = cityid.longitude
        addresses = search(lat, lon)
        address_paginator = Paginator(addresses, 10)
        page_num = request.GET.get('page', 1)
        page = address_paginator.get_page(page_num)

    context = {
        'addresses': addresses,
        "city": cityid,
        "presets": presets,
        "page": page,
    }

    return render(request, 'flikcr_api/index.html', context)


# Index Page
def index(request):
    presets = Preset.objects.all()

    context = {
        "presets": presets,
    }
    return render(request, 'flikcr_api/index.html', context)


# Lon and Lat search page
def searchLatLon(request):
    presets = Preset.objects.all()
    lon = ""
    lat = ""
    addresses = ""
    page = ""
    if request.method == 'POST':
        lon = request.POST.get('longitude')
        lat = request.POST.get('latitude')
        addresses = search(lat, lon)
        address_paginator = Paginator(addresses, 10)
        page_num = request.GET.get('page', 1)
        page = address_paginator.get_page(page_num)

    context = {
        "page": page,
        "addresses": addresses,
        "presets": presets,
        "longitude": lon,
        "latitude": lat,

    }
    return render(request, 'flikcr_api/index.html', context)


global mah


# favourites Page
def favourites(request):
    return render(request, 'flikcr_api/fav.html', {})


# Add presets in database
def add(request):
    # Send new object to the model
    presets = Preset.objects.all()
    form = PresetForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PresetForm()

    context = {
        "presets": presets,
        "form": form
    }

    return render(request, 'flikcr_api/editePresets.html', context)
