from django.contrib import admin
from .models import Booking, GalleryImage, Contact, NewsletterSubscriber, Service
# Register your models here

admin.site.register([Booking, GalleryImage, Contact,
                    NewsletterSubscriber, Service])
