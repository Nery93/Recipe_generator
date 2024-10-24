from pydantic import BaseModel
from typing import List

class Recipe(BaseModel):
    title: str
    ingredients: List[str]
    instructions: List[str]
    