from django.contrib import admin

from .models import product,orders,contact
admin.site.register(contact)
admin.site.register(product)
admin.site.register(orders)