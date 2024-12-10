from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class GroupMember(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    group_id = models.ForeignKey('Group', on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user_id.username + ' - ' + self.group_id.name

class GroupRanking(models.Model):
    id = models.AutoField(primary_key=True)
    group_id = models.OneToOneField(Group, on_delete=models.CASCADE, related_name='ranking')
    total_points = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.group_id.name