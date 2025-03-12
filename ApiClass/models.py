from django.db import models

# Create your models here.
class UserData(models.Model):

    user_name= models.CharField(max_length=50,null=True)
    user_pass= models.CharField(max_length=50,null=True)  

    def __str__(self):
        return f"{self.user_name} {self.user_pass}"  

class Category(models.Model):

    category_name = models.CharField(max_length=50,null=True)

    def __str__(self):
        return f"{self.category_name}"
         
class Product(models.Model):
    category_num = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    product_name= models.CharField(max_length=50,null=True)
    price= models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product_name} {self.price}"