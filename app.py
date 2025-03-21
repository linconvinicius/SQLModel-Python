from sqlmodel import SQLModel, Field

class Usuario(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nome: str
    idade: int
    email: str

sqllite_file_name = "database.db"
connection_string = f"sqlite:///{sqllite_file_name}"