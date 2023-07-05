from django.contrib import admin
from .models import *
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from django.utils.safestring import mark_safe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Category
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name', )}
    list_display_links = ('name', )


class ReviewInline(admin.StackedInline):
    # Attaching product reviews
    model = Review
    readonly_fields = ('name', 'email')
    extra = 1


class ProductResource(resources.ModelResource):
    # Resource class for Product model
    category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'name'))

    class Meta:
        model = Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Product
    list_display = (
        'id', 'name', 'slug', 'price', 'get_image', 
        'available', 'created', 'updated'
        )
    list_filter = ('available', 'created', 'updated')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ('name', )

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='50' ")
    
    get_image.short_description = 'Image'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # Review
    list_display = (
        'name', 
        'text', 
        'email', 
        'product',
        )
    list_display_links = ('name', )
    readonly_fields = ('name', 'email')
    list_display_links = ('name', )
