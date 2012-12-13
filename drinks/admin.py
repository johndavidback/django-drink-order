__author__ = 'john.back'


from django.contrib import admin
from drinks.models import Drink, DrinkOrder


admin.site.register(Drink)
admin.site.register(DrinkOrder)