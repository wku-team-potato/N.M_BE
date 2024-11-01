from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import User
from profiles.models import Profile, ProfileRecord

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user_id=instance, height=None, weight=None)
        