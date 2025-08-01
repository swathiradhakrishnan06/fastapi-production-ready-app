from datetime import datetime
from pydantic import BaseModel, EmailStr

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
        # This allows Pydantic to read data from SQLAlchemy models and convert them to Pydantic models
        # without needing to convert them to dictionaries first.
        # It is useful when you want to return SQLAlchemy models directly in your FastAPI endpoints.   

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True



