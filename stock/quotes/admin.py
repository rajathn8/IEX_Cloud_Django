from django.contrib import admin


# Register your models here.

# admin area

from .models import Stock

admin.site.register(Stock)
 