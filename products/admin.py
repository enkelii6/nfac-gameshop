from django.contrib import admin

from products.models import Product, Game, Genre

admin.site.register(Product)
admin.site.register(Game)
admin.site.register(Genre)
