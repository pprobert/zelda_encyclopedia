from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=500)
    ingredient_1 = models.CharField(max_length=500)
    ingredient_2 = models.CharField(max_length=500)
    ingredient_3 = models.CharField(max_length=500)
    pub_date = models.DateTimeField("date published")

 