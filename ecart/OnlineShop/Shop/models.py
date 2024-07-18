from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=350)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="Shop/images", default="")

    def __str__(self):
        return self.product_name
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=65, default="")
    phone = models.CharField(max_length=15, default="")
    desc = models.TextField(max_length=5000, default="")
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.TextField(max_length=5000)
    amount = models.IntegerField(default="0")
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, default="")    
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250, default="")
    city = models.CharField(max_length=90)
    state = models.CharField(max_length=90)
    zip_code = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.TextField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."

