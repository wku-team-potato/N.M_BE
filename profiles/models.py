from django.db import models
from django.utils import timezone

class Profile(models.Model):
    user_profile_id = models.BigAutoField(primary_key=True)
    user_id = models.OneToOneField('user.User', on_delete=models.CASCADE)
    # birthday = models.DateField(null=True)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user_id.username}'s profile"
    
    class Meta:
        db_table = 'profile'
        ordering = ['user_id']

class ProfileRecord(models.Model):
    user_profile_record_id = models.BigAutoField(primary_key=True)
    user_profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    recorded_at = models.DateTimeField(default=timezone.now, help_text="체중 기록일")

    class Meta:
        db_table = 'profile_record'
        ordering = ['-recorded_at']
        # indexes = [
        #     models.Index(fields=['-recorded_at'], name='idx_recorded_at'),
        #     models.Index(fields=['user_profile_id', '-recorded_at'], name='idx_user_profile_recorded')
        # ]

# class Profile(models.Model):
#     user_profile_id = models.BigAutoField(primary_key=True)
#     user_id = models.OneToOneField('user.User', on_delete=models.CASCADE)
#     birthday = models.DateField(null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return f"{self.user_id.username}'s profile"
    
#     class Meta:
#         db_table = 'profile'
#         ordering = ['user_id']

# class WeightRecord(models.Model):
#     user_profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     height = models.FloatField()
#     weight = models.FloatField()
#     recorded_at = models.DateTimeField(default=timezone.now, help_text="체중 기록일")
#     created_at = models.DateTimeField(auto_now_add=True, help_text="레코드 생성일")
    
#     @classmethod
#     def get_weight_changes(cls, user_profile_id, days=5):
#         start_date = timezone.now() - timezone.timedelta(days=days)
        
#         records = cls.objects.filter(
#             user_profile_id=user_profile_id,
#             recorded_at__gte=start_date
#         ).order_by('recorded_at')
        
#         return records
    
#     def get_weight_difference(self):
#         previous_record = WeightRecord.objects.filter(
#             user_profile_id=self.user_profile_id,
#             recorded_at__lt=self.recorded_at
#         ).order_by('-recorded_at').first()
        
#         if previous_record:
#             return self.weight - previous_record.weight
        
#         return 0
    
#     def __str__(self):
#         return f"{self.profile.user_id.username}'s weight: {self.weight}kg at {self.recorded_at}"
    
#     class Meta:
#         db_table = 'weight_record'
#         ordering = ['-recorded_at']
#         indexes = [
#             models.Index(fields=['-recorded_at'], name='idx_recorded_at'),
#             models.Index(fields=['user_profile_id', '-recorded_at'], name='idx_user_profile_recorded')
#         ]