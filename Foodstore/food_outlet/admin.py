from django.contrib import admin
from .models import Chef, Food

# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    # readonly_fields= ("slug",)               
    prepopulated_fields= {"slug": ("name", )}
    list_filter= ("name", "chef", "rating")
    list_display= ("name", "chef",)

admin.site.register(Food, FoodAdmin)
admin.site.register(Chef)

