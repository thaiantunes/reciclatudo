from sqlalchemy import Column, Integer, Float, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Morador(Base):
    __tablename__ = "moradores"

    id_morador = Column(Integer, primary_key=True, index=True)
    nome = Column(String(200), index=True)
    cep = Column(String(8), index=True)
    logradouro = Column(String(200))
    bairro = Column(String(50))
    ddd = Column(Integer)
    telefone = Column(String(15))
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(80))

class Parceiro(Base):
    __tablename__ = "parceiros"

    id_parceiro = Column(Integer, primary_key=True, index=True)
    nome_instituicao = Column(String(200), index=True)
    responsavel = Column(String(200), index=True)
    cep = Column(String(8), index=True)
    logradouro = Column(String(200))
    bairro = Column(String(50))
    ddd = Column(Integer)
    telefone = Column(String(15))
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(80))

class Coleta(Base):
    __tablename__ = "coletas"

    id_coleta = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    data = Column(String(8), nullable=False)
    turno = Column(String(10), nullable=False)
    quantidade = Column(Integer, nullable=False)
