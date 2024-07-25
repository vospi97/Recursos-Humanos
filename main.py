# main.py
from fastapi import FastAPI
from app import create_app


app = create_app()
app.title = "Gestión de Recursos Humanos"
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)