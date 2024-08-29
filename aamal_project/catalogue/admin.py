from django.contrib import admin
from .models import Category, SubCategory, Product

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1

class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name',)
    search_fields = ('cat_name',)
    inlines = [SubCategoryInline]

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('subcat_name', 'parent_category')
    search_fields = ('subcat_name',)
    list_filter = ('parent_category',)
    inlines = [ProductInline]

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'is_avilable', 'category', 'subcategory')
    search_fields = ('product_name', 'category__cat_name', 'subcategory__subcat_name')
    list_filter = ('category', 'subcategory', 'is_avilable')

# Register models with admin site
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
