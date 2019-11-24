from django.contrib import admin

from .models import Retailer, Store, Order, Item

class StoreInLine(admin.TabularInline):
    model = Store

class RetailerAdmin(admin.ModelAdmin):
    inlines = [
        StoreInLine,
    ]

class ItemInLine(admin.TabularInline):
    model = Item

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ItemInLine
    ]

admin.site.register(Retailer,RetailerAdmin)
admin.site.register(Order,OrderAdmin)