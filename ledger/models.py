from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.name)
    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.name)])

class Recipe(models.Model):
    name = models.CharField(max_length=100)

class RecipeIngredient(models.Model):
    quantity = models.PositiveIntegerField(null=False)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)