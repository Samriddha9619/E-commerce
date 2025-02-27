from django.contrib import admin

from .models import product
from .models import contact
admin.site.register(contact)
admin.site.register(product)