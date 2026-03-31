from django.contrib import admin
from .models import Gallery, Service, Testimonial, ContactMessage


# Gallery Admin
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'height')
    list_filter = ('category',)
    search_fields = ('title', 'description')
    list_editable = ('height',)
    ordering = ('title',)


# Service Admin
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon')
    search_fields = ('title', 'description')
    ordering = ('title',)


# Testimonial Admin
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'rating')
    list_filter = ('rating',)
    search_fields = ('name', 'role', 'message')
    ordering = ('-rating',)


# Contact Message Admin
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'service', 'created_at')
    list_filter = ('service', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)