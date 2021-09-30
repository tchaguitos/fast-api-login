from typing import Optional

from main import app

@app.get("/")
def index():
    return {"Olá": "Mundo"}

@app.get("/usuarios/{id_usuario}")
def consultar_usuario(id_usuario: int, q: Optional[str] = None):
    return { "id": id_usuario, "q": q }
