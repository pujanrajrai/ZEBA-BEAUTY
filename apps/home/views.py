from .forms import BookingForm, ContactForm, NewsletterSubscriptionForm
from .models import GalleryImage, Service
from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            return redirect('success')
    else:
        form = NewsletterSubscriptionForm()

    context = {
        "form": form,
        "images": GalleryImage.objects.all(),
        "services": Service.objects.all()
    }
    return render(request, 'home.html', context)


def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            # Send an email
            # send_mail(
            #     contact.subject,
            #     contact.message,
            #     contact.email,
            #     ['your-email@example.com'],  # Replace with your email address
            #     fail_silently=False,
            # )
            return redirect('success')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def booknow(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or wherever you want
            return redirect('success')
    else:
        form = BookingForm()
    context = {
        "form": form
    }
    return render(request, 'booknow.html', context)


def success(request):
    context = {
        "bg": True
    }
    return render(request, 'success.html', context)


def subscribe_view(request):
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        return redirect('/')
