from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название рецепта")
    description = models.TextField(verbose_name="Описание рецепта")

    def str(self):
        return self.title

class Ingredient(models.Model):
    UNITS = [
        ('граммы', 'Граммы'),
        ('килограммы', 'Килограммы'),
        ('миллилитры', 'Миллилитры'),
        ('литры', 'Литры'),
        ('штуки', 'Штуки'),
    ]

    name = models.CharField(max_length=255, verbose_name="Название ингредиента")
    quantity = models.FloatField(verbose_name="Количество")
    unit = models.CharField(max_length=20, choices=UNITS, verbose_name="Единица измерения")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")

    def str(self):
        return f"{self.name} ({self.quantity} {self.unit})"


