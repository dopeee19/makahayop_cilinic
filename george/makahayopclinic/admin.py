# admin.py
from django.contrib import admin
from .models import Appointment, Vet, Service, Feedback,User

# Register models with the admin site
admin.site.register(Appointment)
admin.site.register(Vet)
admin.site.register(Service)
admin.site.register(Feedback)
admin.site.register(User)