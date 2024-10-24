from fastapi import APIRouter
from app.models.recipe import Recipe
from typing import List

router = APIRouter()

@router.get("/recipes/", response_model=List[Recipe])
def get_recipes(ingredients: str):
    # Aqui você integrará a lógica para buscar receitas
    # Por enquanto, retornaremos uma receita fictícia
    return [
        {
            "title": "Chocolate Cake",
            "ingredients": ["flour", "chocolate", "sugar", "eggs"],
            "instructions": "Mix all ingredients and bake for 30 minutes."
        }
    ]