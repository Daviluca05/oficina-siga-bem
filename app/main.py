# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Banco de dados (SQLite local; use PostgreSQL em produção)
DATABASE_URL = "sqlite:///./siga_bem.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Modelo de dados
class Servico(Base):
    __tablename__ = "servicos"

    id = Column(Integer, primary_key=True, index=True)
    cliente = Column(String, nullable=False)
    veiculo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    data_servico = Column(DateTime, default=datetime.utcnow)

# Cria as tabelas
Base.metadata.create_all(bind=engine)

# Esquema de entrada e saída da API
class ServicoCreate(BaseModel):
    cliente: str
    veiculo: str
    descricao: str

class ServicoOut(ServicoCreate):
    id: int
    data_servico: datetime

    class Config:
        orm_mode = True

# Inicializa app
app = FastAPI(title="API Oficina Siga Bem")

# Dependência para acessar DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rotas
from fastapi import Depends

@app.post("/servicos/", response_model=ServicoOut)
def criar_servico(servico: ServicoCreate, db=Depends(get_db)):
    db_servico = Servico(**servico.dict())
    db.add(db_servico)
    db.commit()
    db.refresh(db_servico)
    return db_servico

@app.get("/servicos/", response_model=List[ServicoOut])
def listar_servicos(db=Depends(get_db)):
    return db.query(Servico).all()

@app.get("/servicos/{id}", response_model=ServicoOut)
def obter_servico(id: int, db=Depends(get_db)):
    servico = db.query(Servico).filter(Servico.id == id).first()
    if not servico:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")
    return servico

@app.delete("/servicos/{id}")
def deletar_servico(id: int, db=Depends(get_db)):
    servico = db.query(Servico).filter(Servico.id == id).first()
    if not servico:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")
    db.delete(servico)
    db.commit()
    return {"mensagem": "Serviço excluído com sucesso"}
