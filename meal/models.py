from django.db import models
from django.contrib.auth.models import User

class UserMeal(models.Model):
    
    MEAL_TYPE_CHOICES = [
        ('breakfast', '아침'),
        ('lunch', '점심'),
        ('dinner', '저녁'),
    ]
    
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey('nutrition.Foods', on_delete=models.CASCADE)
    serving_size = models.FloatField(help_text="음식의 양(g)")
    meal_type = models.CharField(max_length=10, help_text="breakfast, lunch, dinner" , choices=MEAL_TYPE_CHOICES)
    date = models.DateField(help_text="YYYY-MM-DD 형식으로 입력")
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'meal_record'
        ordering = ['-created_at']