from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI()

# Banco de dados local
def init_db():
    conn = sqlite3.connect("siga_bem.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Páginas HTML
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def formulario(request: Request):
    return templates.TemplateResponse("formulario.html", {"request": request})

@app.post("/dados", response_class=HTMLResponse)
def salvar_dado(request: Request, nome: str = Form(...), descricao: str = Form(...)):
    conn = sqlite3.connect("siga_bem.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dados (nome, descricao) VALUES (?, ?)", (nome, descricao))
    conn.commit()
    conn.close()
    return templates.TemplateResponse("sucesso.html", {"request": request, "nome": nome})

@app.get("/dados", response_model=List[dict])
def listar_dados():
    conn = sqlite3.connect("siga_bem.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, descricao FROM dados")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "nome": r[1], "descricao": r[2]} for r in rows]
