from store.models import Product
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin import ProductAdmin, OrderAdmin, ProductImageInline
from tags.models import TaggedItem
from .models import User
# from storefront6.store.models import Order, OrderItem
from store.models import Order, OrderItem

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name'),
        }),
    )


class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem


class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline, ProductImageInline]


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)


# class OrderItemInline(GenericTabularInline):
#     model = OrderItem
#
#
# class CustomOrderAdmin(OrderAdmin):
#     inlines = [OrderItemInline]
#
#
# admin.site.unregister(Order)
# admin.site.register(Order, CustomOrderAdmin)
