from passlib.context import CryptContext
import re
from geopy.geocoders import Nominatim
import requests

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

def get_coordinates(address: str):
    geolocator = Nominatim(user_agent="Konkret")
    loc = geolocator.geocode(address)
    return [loc.latitude, loc.longitude]

def get_weather(lat: float, lon: float):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={"b1c7ce8cfdef7802eafd6a2189e8edfb"}&lang=pt_br&units=metric"
    response = requests.get(url)
    return response.json()