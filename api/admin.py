from django.contrib import admin
from .models import Recipe
# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "ingredient_1",
        "ingredient_2",
        "ingredient_3",
    ]

admin.site.register(Recipe, RecipeAdmin)