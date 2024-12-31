from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'ingredient_1', 'ingredient_2', 'ingredient_3', 'created_at', 'updated_at']
