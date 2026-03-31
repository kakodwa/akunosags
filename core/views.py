from django.shortcuts import render, redirect
from .models import Service, Gallery, Testimonial
from .models import ContactMessage
import json


def home(request):
    services = Service.objects.all()
    return render(request, "akuno/index.html",{'services':services})


def about(request):
    return render(request, "akuno/about.html",{'services':services})

def services(request):
    services = Service.objects.all()
    return render(request, "akuno/services.html",{'services':services})


def gallery(request):
    services = Service.objects.all()
    gallery = Gallery.objects.all()
    testimonial = Testimonial.objects.all()
    return render(request, "akuno/gallery.html",{'services':services,'gallery':gallery,'testimonial':testimonial})

def contact(request):
    services = Service.objects.all()
    return render(request, "akuno/contact.html",{'services':services})