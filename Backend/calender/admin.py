from django.contrib import admin
from .models import ContactFormSubmission

@admin.register(ContactFormSubmission)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email','mobile', 'select_time', 'selected_day')

