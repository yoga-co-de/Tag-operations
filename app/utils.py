from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    byte_length = len(password.encode("utf-8"))

    print("PASSWORD:", password)
    print("BYTE LENGTH:", byte_length)

    if byte_length > 72:
        raise ValueError(f"Password too long: {byte_length} bytes")

    return pwd_context.hash(password)