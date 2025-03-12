
from django.db import models

# Create your models here.
# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=100)
#     published_date = models.DateField()
#     isbn = models.CharField(max_length=13)
#     pages = models.IntegerField()

#     def __str__(self):
#         return self.title


class Product(models.Model):
    product_name = models.CharField(max_length=50,null=True)
    price=models.FloatField(default=0)
    product_code=models.IntegerField(default=0)
    gst=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product_name} ({self.product_code}) {self.price}"






