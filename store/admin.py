from django.contrib import admin
from .models import * 

class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('date_sent',)
# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)