from home.sendemail import SendEmail
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
        data = request.POST
        form = ContactForm(data)
        if form.is_valid():
            contact = form.save()
            sendemail = SendEmail()
            sendemail.send_email_to_client(
                email=[data.get('email')],
                subject="Thank you for contacting us!",
                body_var={
                    "message": "Thank you for reaching out to us. We have received your message and will get back to you as soon as possible.",
                    "full_name": data.get('name')
                },
            )

            sendemail.send_email_to_admin(
                subject="Contact Us Form Received",
                body_var={
                    "message": f"We have received a contact us form from {data.get('name')}.",
                    "name": data.get("name"),
                    "email": data.get("email"),
                    "subject": data.get("subject"),
                    "contact_message": data.get("message"),
                    "phone_number": data.get('phone_number'),
                    "contact": "contact",
                },
            )
            return redirect('success')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def booknow(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            import pdb
            pdb.set_trace()
            # Send email to the client
            sendemail = SendEmail()
            sendemail.send_email_to_client(
                email=[booking.email],
                subject="Thank you for booking with us!",
                body_var={
                    "message": "Thank you for booking with us. We have received your request and will confirm the details soon.",
                    "full_name": booking.name,
                },
            )
            # Send email to the admin
            sendemail.send_email_to_admin(
                subject="New Booking Received",
                body_var={
                    "message": f"A new booking request has been received from {booking.name}.",
                    "name": booking.name,
                    "email": booking.email,
                    "phone": booking.phone,
                    "date": booking.date,
                    "time": booking.time,
                    "reason": booking.reason,
                },
            )

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
