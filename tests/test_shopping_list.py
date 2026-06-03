import pytest
from recipes.ingredient import Ingredient
from recipes.recipe import Recipe
from recipes.shopping_list import ShoppingList

class TestShoppingList:
    def test_add_recipe(self):
        recipe = Recipe("Пицца", [Ingredient("Мука", 500, "г")])
        shopping_list = ShoppingList()
        shopping_list.add_recipe(recipe, 2)
        assert len(shopping_list) == 1

    def test_add_recipe_invalid_portions(self):
        recipe = Recipe("Пицца", [Ingredient("Мука", 500, "г")])
        shopping_list = ShoppingList()
        with pytest.raises(ValueError, match="Количество порций должно быть положительным"):
            shopping_list.add_recipe(recipe, 0)

    def test_remove_recipe(self):
        recipe1 = Recipe("Пицца", [Ingredient("Мука", 500, "г")])
        recipe2 = Recipe("Салат", [Ingredient("Огурец", 2, "шт")])
        shopping_list = ShoppingList()
        shopping_list.add_recipe(recipe1, 1)
        shopping_list.add_recipe(recipe2, 1)
        assert len(shopping_list) == 2
        shopping_list.remove_recipe("Пицца")
        assert len(shopping_list) == 1

    def test_get_list_merges_ingredients(self):
        recipe1 = Recipe("Пицца", [Ingredient("Мука", 500, "г")])
        recipe2 = Recipe("Хлеб", [Ingredient("Мука", 300, "г")])
        shopping_list = ShoppingList()
        shopping_list.add_recipe(recipe1, 1)
        shopping_list.add_recipe(recipe2, 1)
        items = shopping_list.get_list()
        assert len(items) == 1
        assert items[0].quantity == 800

    def test_get_list_sorted(self):
        recipe = Recipe("Блюдо", [
            Ingredient("Цукини", 100, "г"),
            Ingredient("Арбуз", 1, "шт"),
            Ingredient("Баклажан", 2, "шт")
        ])
        shopping_list = ShoppingList()
        shopping_list.add_recipe(recipe, 1)
        items = shopping_list.get_list()
        names = [ing.name for ing in items]
        assert names == sorted(names)

    def test_add_shopping_lists(self):
        list1 = ShoppingList()
        list2 = ShoppingList()
        recipe = Recipe("Пицца", [Ingredient("Мука", 500, "г")])
        list1.add_recipe(recipe, 1)
        list2.add_recipe(recipe, 1)
        combined = list1 + list2
        assert len(combined) == 2
        assert len(list1) == 1
        assert len(list2) == 1