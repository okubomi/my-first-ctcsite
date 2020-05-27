from django.contrib import admin

# Register your models here.
from .models import Item
from .models import Customer
from .models import Cart

admin.site.register(Item)
admin.site.register(Customer)
admin.site.register(Cart)
