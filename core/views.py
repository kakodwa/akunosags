from django.shortcuts import render, redirect
from .models import Service, Gallery, Testimonial
from .models import ContactMessage
import json

def home(request):
    services = Service.objects.all()
    gallery = Gallery.objects.all()
    testimonials = Testimonial.objects.all()

    return render(request, "akuno/akuno.html", {
        "services": services,
        "gallery": gallery,
        "testimonials": testimonials
    })

def home(request):
    gallery = Gallery.objects.all()
    services = list(Service.objects.values())
    testimonials = list(Testimonial.objects.values())

    gallery_data = []
    for g in gallery:
        gallery_data.append({
            "id": g.id,
            "category": g.category,
            "title": g.title,
            "desc": g.description,
            "icon": g.icon,
            "color": g.color,
            "height": g.height,
            "accent": g.accent,
            "image": g.image.url if g.image else ""
        })

    return render(request, "akuno/akuno.html", {
        "gallery_json": json.dumps(gallery_data),
        "services_json": json.dumps(services),
        "testimonials_json": json.dumps(testimonials),
        "services":Service.objects.all(),
        "testimonials":Testimonial.objects.all(),
    })


def contact(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            first_name=request.POST.get("firstName"),
            last_name=request.POST.get("lastName"),
            email=request.POST.get("formEmail"),
            phone=request.POST.get("formPhone"),
            service=request.POST.get("service"),
            message=request.POST.get("message"),
        )
        return redirect("home")