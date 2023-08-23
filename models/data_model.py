from sqlalchemy import Column, Integer, Float, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Morador(Base):
    __tablename__ = "moradores"

    id_morador = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cep = Column(String, index=True)
    logradouro = Column(String)
    bairro = Column(String)
    ddd = Column(Integer)
    telefone = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Parceiro(Base):
    __tablename__ = "parceiros"

    id_parceiro = Column(Integer, primary_key=True, index=True)
    nome_instituicao = Column(String, index=True)
    responsavel = Column(String, index=True)
    cep = Column(String, index=True)
    logradouro = Column(String)
    bairro = Column(String)
    ddd = Column(Integer)
    telefone = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Coleta(Base):
    __tablename__ = "coletas"

    id_coleta = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    data = Column(String, nullable=False)
    turno = Column(String, nullable=False)
    quantidade = Column(Integer, nullable=False)
