from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, verbose_name='닉네임', null=False, blank=False, unique=True)
    total_points = models.IntegerField(default=0)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'profile'
        ordering = ['user_id']

class HeightWeightRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    created_at = models.DateField(default=timezone.now, help_text="체중 기록일")

    class Meta:
        db_table = 'height_weight_record'
        ordering = ['-created_at']