from django.db import models
from cloudinary.models import CloudinaryField


class Gallery(models.Model):
    CATEGORY_CHOICES = [
        ('Accessories', 'Accessories'),
        ('System Design', 'System Design'),
        ('Site Assessment', 'Site Assessment'),
        ('Installation', 'Installation'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = CloudinaryField('gallery', blank=True, null=True)

    # UI fields (for your design)
    icon = models.CharField(max_length=50, default='image')
    color = models.CharField(max_length=20, default='#162335')
    accent = models.CharField(max_length=20, default='#C9A84C')
    height = models.IntegerField(default=200)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField('services', blank=True, null=True)
    icon = models.CharField(max_length=50, default='zap')

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=150)
    message = models.TextField()
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.name

    @property
    def initials(self):
        return "".join([n[0].upper() for n in self.name.split() if n])


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    service = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


