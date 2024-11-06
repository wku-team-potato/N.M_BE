from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PointTransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points_changed = models.IntegerField()
    transaction_type = models.CharField(max_length=10)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)