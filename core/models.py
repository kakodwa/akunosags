from django.db import models


class Gallery(models.Model):
    CATEGORY_CHOICES = [
        ('consulting', 'Consulting'),
        ('analytics', 'Analytics'),
        ('projects', 'Projects'),
        ('team', 'Team'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='gallery/', blank=True, null=True)

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


