from sqlmodel import SQLModel, Field
from typing import Optional
from models.user import User

class userSchema(User, SQLModel, table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: str
    time: str
    img_location: str