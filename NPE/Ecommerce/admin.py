

# Register your models here.

from django.contrib import admin
from .models import ProductCategory,ProductSubCategory,Product,Contact

admin.site.register(ProductCategory)
admin.site.register(ProductSubCategory)
admin.site.register(Product)
admin.site.register(Contact)
