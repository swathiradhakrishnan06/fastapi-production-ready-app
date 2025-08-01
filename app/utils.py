# from passlib.context import CryptContext
from passlib.hash import argon2

# Hashing algorithm(bcrypt)for passwords
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
pwd_context = argon2

def hash(password: str):
    return pwd_context.hash(password)