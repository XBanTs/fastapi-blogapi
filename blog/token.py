from datetime import datetime, timedelta
from jose import JWTError, jwt
from . import schemas
from .config import settings


# def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
def create_access_token(data: dict ):
  to_encode = data.copy()
  expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
  return encoded_jwt

def verify_token(token: str, credentials_exception):
  try:
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    email: str = payload.get("sub")
    if email is None:
      raise credentials_exception
    token_data = schemas.TokenData(email=email)
  except JWTError:
     raise credentials_exception