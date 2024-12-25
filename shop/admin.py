from django.contrib import admin
from .models import *


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  
    list_display = ("name", "description","image","slug")

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category","image","description")

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'phone', 'subject','message', 'created_at')  
    search_fields = ('email', 'subject')  
    list_filter = ('created_at',)  

admin.site.register(Category, CategoryAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Contact, ContactAdmin)
