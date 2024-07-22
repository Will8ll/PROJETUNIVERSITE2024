from django.contrib import admin
from .models import Subscriber
from .models import Registration

admin.site.register(Subscriber)

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact_number')