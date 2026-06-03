import pytest
from recipes.ingredient import Ingredient
from recipes.recipe import Recipe

class TestRecipe:
    def test_creation(self):
        ingredients = [Ingredient("Мука", 500, "г")]
        recipe = Recipe("Пицца", ingredients)
        assert recipe.title == "Пицца"
        assert len(recipe.ingredients) == 1

    def test_add_ingredient_new(self):
        recipe = Recipe("Салат")
        recipe.add_ingredient(Ingredient("Огурец", 2, "шт"))
        assert len(recipe) == 1

    def test_add_ingredient_duplicate(self):
        recipe = Recipe("Салат")
        recipe.add_ingredient(Ingredient("Огурец", 2, "шт"))
        recipe.add_ingredient(Ingredient("Огурец", 3, "шт"))
        assert len(recipe) == 1
        assert recipe.ingredients[0].quantity == 5

    def test_scale(self):
        recipe = Recipe("Пицца", [Ingredient("Мука", 500, "г")])
        scaled = recipe.scale(2)
        assert scaled is not recipe
        assert scaled.ingredients[0].quantity == 1000

    def test_scale_invalid_ratio(self):
        recipe = Recipe("Пицца", [Ingredient("Мука", 500, "г")])
        with pytest.raises(ValueError):
            recipe.scale(0)

    def test_len(self):
        recipe = Recipe("Салат")
        recipe.add_ingredient(Ingredient("Огурец", 2, "шт"))
        recipe.add_ingredient(Ingredient("Помидор", 3, "шт"))
        assert len(recipe) == 2
