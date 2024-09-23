from django.contrib import admin
from .models import Booking, Contact, NewsletterSubscriber, GalleryImage, Service, Email


# Custom Action to Mark as Read
def mark_as_read(modeladmin, request, queryset):
    queryset.update(is_read=True)
    modeladmin.message_user(
        request, "Selected items have been marked as read.")


# Custom Admin for Booking
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone',
                    'date', 'time', 'reason', 'is_read']
    list_filter = ['is_read', 'date']
    search_fields = ['name', 'email', 'phone', 'reason']
    ordering = ['is_read', 'date', 'time']
    actions = [mark_as_read]  # Add custom action

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Prioritize unread bookings first
        return qs.order_by('is_read', 'date')


# Custom Admin for Contact
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject',
                    'phone_number', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'phone_number']
    ordering = ['is_read', 'created_at']
    actions = [mark_as_read]  # Add custom action

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Prioritize unread contacts first
        return qs.order_by('is_read', '-created_at')


# Admin for NewsletterSubscriber
@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at']
    search_fields = ['email']
    ordering = ['subscribed_at']


# Admin for GalleryImage
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['caption', 'image']
    search_fields = ['caption']
    ordering = ['id']


# Admin for Service
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description']
    search_fields = ['name', 'description']
    ordering = ['name']


# Admin for Email
@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['email']
    search_fields = ['email']
    ordering = ['email']
