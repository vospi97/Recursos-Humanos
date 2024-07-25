# main.py
from fastapi import FastAPI
from app import create_app


app = create_app()
app.title = "Gestión de Recursos Humanos"
app.version = "0.1.0"

# Esta app es para probar si el puerto funciona bien
@app.get("/")
async def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)