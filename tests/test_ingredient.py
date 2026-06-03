import pytest
from recipes.ingredient import Ingredient

class TestIngredient:
    def test_creation(self):
        ing = Ingredient("Мука", 500.0, "г")
        assert ing.name == "Мука"
        assert ing.quantity == 500.0
        assert ing.unit == "г"

    def test_quantity_positive(self):
        with pytest.raises(ValueError, match="Количество должно быть положительным"):
            Ingredient("Соль", -10, "г")

    def test_str(self):
        ing = Ingredient("Мука", 500.0, "г")
        assert str(ing) == "Мука: 500.0 г"

    def test_repr(self):
        ing = Ingredient("Мука", 500.0, "г")
        assert repr(ing) == "Ingredient('Мука', 500.0, 'г')"

    def test_eq_same_name_unit(self):
        ing1 = Ingredient("Мука", 500, "г")
        ing2 = Ingredient("Мука", 1000, "г")
        assert ing1 == ing2

    def test_eq_different_name(self):
        ing1 = Ingredient("Мука", 500, "г")
        ing2 = Ingredient("Сахар", 500, "г")
        assert ing1 != ing2