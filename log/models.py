from django.db import models

# Create your models here

class Food (models.Model):
    description = models.TextField()
    calories = models.IntegerField()
    gramsProtein = models.IntegerField()
    gramsCarb = models.IntegerField()
    gramsFat = models.IntegerField()
    gramsFiber = models.IntegerField()

class SingleDayFood(models.Model):
    date = models.DateField()
    breakfastFoods = Food.objects
    lunchFoods = Food.objects
    dinnerFoods = Food.objects

