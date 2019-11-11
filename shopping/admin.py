from django.contrib import admin

from .models import Retail, Store, Order, Item

class StoreInLine(admin.TabularInline):
    model = Store

class RetailAdmin(admin.ModelAdmin):
    inlines = [
        StoreInLine,
    ]

class ItemInLine(admin.TabularInline):
    model = Item

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ItemInLine
    ]

admin.site.register(Retail,RetailAdmin)
admin.site.register(Order,OrderAdmin)