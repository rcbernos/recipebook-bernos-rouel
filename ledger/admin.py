from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline, RecipeImageInline]


class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
