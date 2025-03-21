from app import Usuario, engine
from sqlmodel import Session, select

with Session(engine) as session:
    usuario = Usuario(nome="Roberval", idade=32, email="teste@gmail.com")
    session.add(usuario)
    session.commit()

    statement = select(Usuario)
    results = session.exec(statement).all()
    print(results)