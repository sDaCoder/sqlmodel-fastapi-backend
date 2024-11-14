from sqlmodel import SQLModel, Field

class User(SQLModel):
    name: str
    email: str = Field(unique=True)
    age: int