from django.db import models

# Create your models here.
class Foods(models.Model):
    food_code = models.BigAutoField(primary_key=True)
    food_name = models.CharField(max_length=20, null=False)
    serving_size = models.CharField(max_length=20, null=False, help_text='g')
    energy = models.FloatField(null=False, help_text='kcal')
    carbohydrate = models.FloatField(null=False, help_text='g')
    sugars = models.FloatField(null=True, help_text='g')
    fat = models.FloatField(null=True, help_text='g')
    protein = models.FloatField(null=False, help_text='g')
    calcium = models.FloatField(null=True, help_text='mg')
    phosphorus = models.FloatField(null=True, help_text='mg')
    sodium = models.FloatField(null=True, help_text='mg')
    potassium = models.FloatField(null=True, help_text='mg')
    magnesium = models.FloatField(null=True, help_text='mg')
    iron = models.FloatField(null=True, help_text='mg')
    zinc = models.FloatField(null=True, help_text='mg')
    cholesterol = models.FloatField(null=True, help_text='mg')
    trans_fat = models.FloatField(null=True, help_text='g')
    

    def __str__(self):
        return self.food_name

    class Meta:
        verbose_name = 'Food Nutrition'
        verbose_name_plural = 'Food Nutrition'