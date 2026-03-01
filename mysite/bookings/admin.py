from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "number",
        "time",
        "slot",
        "registered_time",
        "isValid",
    )

    list_filter = (
        "time",
        "isValid",
    )

    search_fields = (
        "email",
        "number",
    )
    #newest bookings displayed based on registered time.
    ordering = ("-registered_time",)

    readonly_fields = ("registered_time",)

    #layout on the admin page.
    fieldsets = (
        ("User Info", {
            "fields": ("email", "number")
        }),
        ("Booking Info", {
            "fields": ("time", "slot")
        }),
        ("System", {
            "fields": ("registered_time", "isValid")
        }),
    )