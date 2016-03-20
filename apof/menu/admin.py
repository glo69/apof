from django.contrib import admin
from menu.models import Restaurant, Ingredient, Menu, Cart
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Ingredient)
admin.site.register(Menu)
admin.site.register(Cart)
