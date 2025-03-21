from app import Usuario, engine
from sqlmodel import Session

with Session(engine) as session:
    usuario = Usuario(nome="Roberval", idade=32, email="teste@gmail.com")