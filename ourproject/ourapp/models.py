from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    CATEGORY_TYPE_CHOICES = [
        ('burmese', 'Burmese Medicine'),
        ('english', 'English Medicine'),
    ]

    category_name = models.CharField(max_length=255)
    category_type = models.CharField(max_length=100, choices=CATEGORY_TYPE_CHOICES)

    def str(self):
        return f"{self.category_name} ({self.get_category_type_display()})"
    
class Disease(models.Model):
    item_photo = models.ImageField(upload_to='photos',blank=True, null=True)
    disease_name = models.CharField(max_length=255)
    disease_symptom = models.TextField()
    def __str__(self):
        return self.disease_name

class Supplier(models.Model):
    company_name = models.CharField(max_length=255)
    company_phnumber = models.CharField(blank=False)
    company_location = models.TextField(blank=True, null= True)
    order_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.company_name
    



class Item(models.Model):
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete= models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete= models.CASCADE, blank=True, null=True)
    item_photo = models.ImageField(upload_to='photos')
    item_name = models.CharField(max_length=255)
    item_quatity =models.PositiveIntegerField()
    item_price = models.PositiveIntegerField()
    purcharse_price = models.PositiveIntegerField(default=0)
    item_description = models.TextField()
    exp_date = models.DateField()
    brand_name = models.CharField(max_length=255, blank=True, null=True)
    batch_number = models.CharField(max_length=100, blank=True, null=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    stock_minimum = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.item_name


class Cart(models.Model):
    total_amount =models.PositiveIntegerField(default=0)
    created_date = models.DateField(auto_now_add= True)
    def update_total_amount(self):
        total_amount = sum(cp.price for cp in self.cartproduct_set.all())
        self.total_amount = total_amount
        self.save()
    
class CartProduct(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
 



# models.py
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def str(self):
        return f"{self.user.username} - {self.item.item_name}"
    

class StockHistory(models.Model):
    ACTION_CHOICES = [
        ('in', 'Stock In'),
        ('out', 'Stock Out'),
    ]

    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True, null=True)

    def str(self):
        return f"{self.item.item_name} - {self.get_action_display()} - {self.quantity}"
    

    
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    address = models.TextField()

    def str(self):
        return self.user.username



class Sale(models.Model):
    invoice_no = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # salesperson
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    def str(self):
        return f"Invoice {self.invoice_no}"

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items")
    item = models.ForeignKey('Item', on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def str(self):
        return f"{self.item.item_name} - {self.quantity} pcs"
# class SaleItem(models.Model):
#     sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items")
#     item = models.ForeignKey('Item', on_delete=models.SET_NULL, null=True)
#     quantity = models.PositiveIntegerField()
#     price = models.PositiveIntegerField()

    # def str(self):
    #     return f"{self.item.item_name} - {self.quantity} pcs"


