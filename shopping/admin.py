from django.contrib import admin

from .models import Retail, Store, Order, Item

admin.site.register(Retail)
admin.site.register(Store)
admin.site.register(Order)
admin.site.register(Item)