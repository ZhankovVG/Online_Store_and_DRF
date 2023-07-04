from django.db import models
from slugify import slugify


class Category(models.Model):
    # Category
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    # All items
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, db_index=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Product, self).save(*args, **kwargs)


class Review(models.Model):
    # Review
    name = models.CharField(max_length=100, db_index=True)
    text = models.TextField(max_length=5000)
    email = models.EmailField()
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parent'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Product')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'