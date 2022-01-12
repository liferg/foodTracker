from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here

class Food (models.Model):
    description = models.CharField(null=True, max_length=120)
    brand = models.CharField(null=True, max_length=120)
    servingSize = models.IntegerField(null=True)
    servingSizeUnit = models.CharField(null=True, max_length=120)
    calories = models.IntegerField(null=True)
    gramsProtein = models.IntegerField(null=True)
    gramsCarb = models.IntegerField(null=True)
    gramsFat = models.IntegerField(null=True)
    gramsFiber = models.IntegerField(null=True)

class SingleDayFood(models.Model):
    date = models.DateField()
    breakfast = models.ForeignKey(Food, blank=True, related_name='breakfastFoods', on_delete=CASCADE)
    lunch = models.ForeignKey(Food, blank=True, related_name='lunchFoods', on_delete=CASCADE)
    dinner = models.ForeignKey(Food, blank=True, related_name='dinnerFoods', on_delete=CASCADE)

class User(models.Model):
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    userName = models.CharField(max_length=120)
    foodDiary = models.ForeignKey(SingleDayFood, blank=True, on_delete=CASCADE)
