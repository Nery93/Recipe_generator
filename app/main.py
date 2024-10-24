from fastapi import FastAPI
from app.routes.recipe import router as recipe_router  # Importação correta

app = FastAPI()
app.include_router(recipe_router, prefix="/api")


@app.get('/')
def read_root():
    return {"message": "Welcome to the Recipe Generator API!"}