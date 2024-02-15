from django.contrib import admin
from .models import store

class stores(admin.ModelAdmin):
    list_display=("name","image")
    readonly_fields = ("id",)
admin.site.register(store,stores)
