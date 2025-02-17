from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Prodeuct(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    in_stock = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        return self.price * self.quantity

class Cart(models.Model):
    product = models.OneToOneField(Prodeuct,on_delete = models.CASCADE)
    quontity = models.PositiveBigIntegerField()

    def __str__(self) :
        return self.product.name
    
