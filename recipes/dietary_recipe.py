from typing import List, Optional
from .recipe import Recipe
from .ingredient import Ingredient

class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients: Optional[List[Ingredient]] = None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio: float) -> 'DietaryRecipe':
        if not self.is_valid_ratio(ratio):
            raise ValueError("Коэффициент масштабирования должен быть положительным числом")
        
        scaled_ingredients = []
        for ing in self.ingredients:
            scaled_ing = Ingredient(ing.name, ing.quantity * ratio, ing.unit)
            scaled_ingredients.append(scaled_ing)
        
        return DietaryRecipe(self.title, self.diet_type, scaled_ingredients)

    def __str__(self) -> str:
        return f"[{self.diet_type}] {self.title}\n" + "\n".join(
            str(ing) for ing in self.ingredients
        )