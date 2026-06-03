from typing import List, Tuple, Dict
from .ingredient import Ingredient
from .recipe import Recipe

class ShoppingList:
    def __init__(self):
        self._items: List[Tuple[Ingredient, str]] = []

    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        
        scaled_recipe = recipe.scale(portions)
        for ing in scaled_recipe.ingredients:
            self._items.append((ing, recipe.title))

    def remove_recipe(self, title: str):
        self._items = [item for item in self._items if item[1] != title]

    def get_list(self) -> List[Ingredient]:
        merged: Dict[Tuple[str, str], float] = {}
        
        for ingredient, recipe_title in self._items:
            key = (ingredient.name, ingredient.unit)
            merged[key] = merged.get(key, 0) + ingredient.quantity
        
        result = [Ingredient(name, quantity, unit) for (name, unit), quantity in merged.items()]
        result.sort(key=lambda ing: ing.name)
        return result

    def __add__(self, other: 'ShoppingList') -> 'ShoppingList':
        new_list = ShoppingList()
        new_list._items = self._items.copy() + other._items.copy()
        return new_list

    def __len__(self) -> int:
        return len(self._items)