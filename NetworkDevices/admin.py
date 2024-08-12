from django.contrib import admin
from NetworkDevices.models import NetworkDevice

# Register your models here.

class NetworkDeviceAdmin(admin.ModelAdmin):
    list_display = ['name','vendor_type','ip_address']
    

admin.site.register(NetworkDevice, NetworkDeviceAdmin)