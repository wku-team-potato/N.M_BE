from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='media/images/items/')
    created_at = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = 'item'


class PurchaseRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'purchase_record'