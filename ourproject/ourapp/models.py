from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=255)
    def __str__(self):
            return self.category_name
    
class Disease(models.Model):
    item_photo = models.ImageField(upload_to='photos',blank=True, null=True)
    disease_name = models.CharField(max_length=255)
    disease_symptom = models.TextField()
    def __str__(self):
        return self.disease_name




class Item(models.Model):
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete= models.CASCADE)
    item_photo = models.ImageField(upload_to='photos')
    item_name = models.CharField(max_length=255)
    item_quatity =models.PositiveIntegerField()
    item_price = models.PositiveIntegerField()
    item_description = models.TextField()
    exp_date = models.DateField()

    def __str__(self):
        return self.item_name
