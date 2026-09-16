from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock_quantity = models.IntegerField()
    image_url = models.CharField(blank=True, null=True, max_length=2083)

    def __str__(self):
        return self.name

class Offer(models.Model):
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    discount = models.FloatField()

    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    """

    def __str__(self):
       # return f"{self.discount}% off on {self.product.name}"
        return self.code
        