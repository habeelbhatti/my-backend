from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone', 'city', 'total_amount', 'discount', 'payment_method', 'created_at']
    search_fields = ['full_name', 'phone', 'email', 'city', 'area']
    list_filter = ['city', 'payment_method', 'created_at']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)  # ✅ correct model name


