from typing import List
from .ingredient import Ingredient

class Recipe:
    def __init__(self, title: str, ingredients: List[Ingredient] = None):
        self.title = title
        self._ingredients = {}
        if ingredients:
            for ing in ingredients:
                self.add_ingredient(ing)

    def add_ingredient(self, ingredient: Ingredient):
        key = (ingredient.name, ingredient.unit)
        if key in self._ingredients:
            self._ingredients[key].quantity += ingredient.quantity
        else:
            self._ingredients[key] = ingredient

    @property
    def ingredients(self) -> List[Ingredient]:
        return list(self._ingredients.values())

    @staticmethod
    def is_valid_ratio(ratio) -> bool:
        try:
            return float(ratio) > 0
        except (TypeError, ValueError):
            return False

    def scale(self, ratio: float) -> 'Recipe':
        if not self.is_valid_ratio(ratio):
            raise ValueError("Коэффициент масштабирования должен быть положительным числом")
        
        scaled_ingredients = []
        for ing in self.ingredients:
            scaled_ing = Ingredient(ing.name, ing.quantity * ratio, ing.unit)
            scaled_ingredients.append(scaled_ing)
        
        return Recipe(self.title, scaled_ingredients)

    def __len__(self) -> int:
        return len(self._ingredients)

    def __str__(self) -> str:
        lines = [f"Рецепт: {self.title}"]
        lines.extend(str(ing) for ing in self.ingredients)
        return "\n".join(lines)

