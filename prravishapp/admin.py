from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(Register)


@admin.register(Enquiry)
class EnquiryUser(admin.ModelAdmin):
    # Specify the fields to display in the list view for the model
    list_display = ['name', 'email', 'phone', 'address', 'city', 'state', 'country', 'interested_product', 'message']


# menu_admin
@admin.register(MenuStarter)
class Starter(admin.ModelAdmin):
    list_display = ['image', 'food_name', 'price', 'food_desc']


@admin.register(MenuMain)
class MainCourse(admin.ModelAdmin):
    list_display = ['image', 'food_name', 'price', 'food_desc']


@admin.register(MenuDrinks)
class Drinks(admin.ModelAdmin):
    list_display = ['image', 'food_name', 'price', 'food_desc']

    
@admin.register(MenuOffers)
class Offers(admin.ModelAdmin):
    list_display = ['image', 'food_name', 'price', 'food_desc']


@admin.register(MenuSpecial)
class Special(admin.ModelAdmin):
    list_display = ['image', 'food_name', 'price', 'food_desc']


# admin
# admin123
