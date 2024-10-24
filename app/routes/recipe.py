# app/routes/recipe.py
from fastapi import APIRouter
from app.models.recipe import Recipe
from typing import List

router = APIRouter()  # Criei uma instancia de roteador

@router.get("/recipes/", response_model=List[Recipe])
def get_recipes(ingredients: str):
    # Aqui vou integrar uma logica para buscar receitas
    return [
        {
            "title": "Chocolate Cake",
            "ingredients": ["flour", "chocolate", "sugar", "eggs"],
            "instructions": ["Mix all ingredients and bake for 30 minutes."]
        }
    ]
