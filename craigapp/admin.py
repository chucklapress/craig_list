from django.contrib import admin
from craigapp.models import Listing, Category, SubCategory, Region

# Register your models here.
admin.site.register(Listing)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Region)

