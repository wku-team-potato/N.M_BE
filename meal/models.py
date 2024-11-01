from django.db import models

class UserMeal(models.Model):
    
    MEAL_TYPE_CHOICES = [
        ('breakfast', '아침'),
        ('lunch', '점심'),
        ('dinner', '저녁'),
    ]
    
    user_meal_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    food_id = models.ForeignKey('nutrition.Foods', on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=10, choices=MEAL_TYPE_CHOICES)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.meal_type} on {self.date}"