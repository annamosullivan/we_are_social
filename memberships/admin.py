from django.contrib import admin
from .models import Membership


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')

admin.site.register(Membership)
