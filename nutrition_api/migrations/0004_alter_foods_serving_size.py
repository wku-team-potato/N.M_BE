# Generated by Django 4.2.16 on 2024-09-24 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition_api', '0003_alter_foods_food_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='serving_size',
            field=models.CharField(max_length=30),
        ),
    ]
