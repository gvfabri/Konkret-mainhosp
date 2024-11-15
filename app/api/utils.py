from passlib.context import CryptContext
import re

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
Tamanho_min_senha = 8

def is_valid_password(password: str) -> bool:
    if len(password) < Tamanho_min_senha:
        return "A senha deve ter pelo menos {Tamanho_min_senha} caracteres."
    if not re.search(r"[A-Z]", password):
        return "A senha deve conter pelo menos uma letra maiúscula."
    if not re.search(r"\d", password):
        return "A senha deve conter pelo menos um número."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "A senha deve conter pelo menos um caractere especial."
    return None

def hash_password(password: str) -> str:
    return pwd_context.hash(password)