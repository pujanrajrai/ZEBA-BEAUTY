from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption or f"Image {self.id}"


class Service(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services/')
    description = models.TextField()

    def __str__(self):
        return self.name


class Email(models.Model):
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email
