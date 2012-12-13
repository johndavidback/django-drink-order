__author__ = 'john.back'

from django.contrib import admin
from drinks.models import Drink, DrinkOrder


class DrinkOrderAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'notes', 'placed', 'fulfilled']

admin.site.register(Drink)
admin.site.register(DrinkOrder, DrinkOrderAdmin)