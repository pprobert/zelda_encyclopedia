from django.db import models
from django.utils import timezone


class Recipe(models.Model):
    name = models.CharField(max_length=500)
    cooking_req = models.CharField(max_length=200, default="in pot")
    ingredient_1 = models.CharField(max_length=500)
    ingredient_2 = models.CharField(max_length=500, null=True, blank=True)
    ingredient_3 = models.CharField(max_length=500, null=True, blank=True)
    ingredient_4 = models.CharField(max_length=500, null=True, blank=True)
    ingredient_5 = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
 
monster_recipes = Recipe.objects.filter(name='Monster', ingredient_1='Monster extract')
vegtable_recipes = Recipe.objects.filter(name__in= ['Vegtable', 'Veggie', 'Herb', 'carrot', 'Radish', 'Stambulb'])
mushroom_recipes = Recipe.objects.filter(name__in=['Mushroom', 'Rushroom', 'Sunshroom', 'Chillshroom', 'Zapshroom', 'Razorshroom', 'Ironshroom', 'Skyshrrom',
'Hylain shroom', 'Stamella shroom', 'Silent shroom', 'Endura shroom', 'Brightcap', 'Big hearty truffle', 'Hearty truffle'])
dark_recipes = Recipe.objects.filter(name='Dark', ingredient_1='dark clump')
curry_recipes = Recipe.objects.filter(name='Curry')
potion_recipe = Recipe.objects.filter(name__in=['Elixir', 'Tonic'])
soup_recipe = Recipe.objects.filter(name__in=['Soup', 'Stew'])