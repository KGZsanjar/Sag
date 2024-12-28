from django import forms
from .models import Recipe, Ingredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description']
        labels = {
            'title': 'Название',
            'description': 'Описание',
        }

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit', 'recipe']
        labels = {
            'name': 'Название ингредиента',
            'quantity': 'Количество',
            'unit': 'Единица измерения',
            'recipe': 'Рецепт',
        }