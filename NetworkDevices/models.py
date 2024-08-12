from django.db import models

class NetworkDevice(models.Model):
    class VendorTextChoices(models.TextChoices):
        CISCO       = "IOS", "Cisco"
        ARISTA      = "EOS", "Arista"
        JUNIPER     = "JUNOS", "Juniper"
        A10         = "ACOS", "A10"
    
    name = models.CharField(max_length=50, blank=False, null=False)
    ip_address = models.GenericIPAddressField(null=False, blank=False)
    vendor_type = models.CharField(max_length=5,choices=VendorTextChoices.choices,
        default=VendorTextChoices.CISCO)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    
