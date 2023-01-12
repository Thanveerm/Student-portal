from django.contrib import admin
from app.models import Registration


class RegistrationAdmin(admin.ModelAdmin):
    list_view = ['id', 'first_name', 'last_name', 'email_id', 'phone', 'address1', 'address2']


admin.site.register(Registration, RegistrationAdmin)
