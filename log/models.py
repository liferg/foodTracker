from django.db import models

# Create your models here

class Food (models.Model):
    description = models.TextField()
    brand = models.TextField()
    servingSize = models.IntegerField()
    servingSizeUnit = models.TextField()
    calories = models.IntegerField()
    gramsProtein = models.IntegerField()
    gramsCarb = models.IntegerField()
    gramsFat = models.IntegerField()
    gramsFiber = models.IntegerField()
    def __init__(self, description, brand, servingSize, servingSizeUnit, calories, gramsProtein, gramsCarb, gramsFat, gramsFiber):
        self.description = description
        self.brand = brand
        self.servingSize = servingSize
        self.servingSizeUnit = servingSizeUnit
        self.calories = calories
        self.gramsProtein = gramsProtein
        self.gramsCarb = gramsCarb
        self.gramsFat = gramsFat
        self.gramsFiber = gramsFiber

class SingleDayFood(models.Model):
    date = models.DateField()
    breakfastFoods = Food.objects
    lunchFoods = Food.objects
    dinnerFoods = Food.objects

