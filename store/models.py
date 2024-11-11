import uuid
from django.db import models

# Create your models here.

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    unique_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    unique_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    image = models.ImageField(upload_to='productImages/',null=True,blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_ordering = models.PositiveIntegerField(null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    @property
    def is_in_stock(self):
        """Returns True if the product is in stock."""
        return self.stock > 0

    def get_discounted_price(self, discount_percent):
        """Calculates the discounted price based on the given percentage."""
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Discount percent must be between 0 and 100.")
        return self.price - (self.price * (discount_percent / 100))
