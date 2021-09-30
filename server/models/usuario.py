from pydantic import BaseModel, EmailStr


class Usuario(BaseModel):
    primeiro_nome: str
    ultimo_nome: str
    nome_de_usuario: str
    email: EmailStr
    senha: str
