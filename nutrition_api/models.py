from django.db import models

# Create your models here.
class Foods(models.Model):
    food_code = models.CharField(max_length=50, primary_key=True)
    food_name = models.CharField(max_length=100)
    representative_food_name = models.CharField(max_length=100)
    food_subcategory = models.CharField(max_length=50)
    serving_size = models.CharField(max_length=30)
    energy = models.FloatField(null=True, help_text='kcal')
    moisture = models.FloatField(null=True, help_text='g')
    protein = models.FloatField(null=True, help_text='g')
    fat = models.FloatField(null=True, help_text='g')
    ash = models.FloatField(null=True, help_text='g')
    carbohydrate = models.FloatField(null=True, help_text='g')
    sugars = models.FloatField(null=True, help_text='g')
    dietary_fiber = models.FloatField(null=True, help_text='g')
    calcium = models.FloatField(null=True, help_text='mg')
    iron = models.FloatField(null=True, help_text='mg')
    phosphorus = models.FloatField(null=True, help_text='mg')
    potassium = models.FloatField(null=True, help_text='mg')
    sodium = models.FloatField(null=True, help_text='mg')
    vitamin_a = models.FloatField(null=True, help_text='μg RAE')
    retinol = models.FloatField(null=True, help_text='μg')
    beta_carotene = models.FloatField(null=True, help_text='μg')
    thiamin = models.FloatField(null=True, help_text='mg')
    riboflavin = models.FloatField(null=True, help_text='mg')
    niacin = models.FloatField(null=True, help_text='mg')
    vitamin_c = models.FloatField(null=True, help_text='mg')
    vitamin_d = models.FloatField(null=True, help_text='μg')
    cholesterol = models.FloatField(null=True, help_text='mg')
    saturated_fat = models.FloatField(null=True, help_text='g')
    trans_fat = models.FloatField(null=True, help_text='g')

    def __str__(self):
        return self.food_name

    class Meta:
        verbose_name = 'Food Nutrition'
        verbose_name_plural = 'Food Nutrition'