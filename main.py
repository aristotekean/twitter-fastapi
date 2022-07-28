# Python
from datetime import date, datetime
from typing import Optional, List
from uuid import UUID

# Pydantic
from pydantic import BaseModel, EmailStr, Field

# FastAPI
from fastapi import FastAPI, status

app = FastAPI()

# Models


class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)


class UserLogin(UserBase):
    password: str = Field(..., min_length=8, max_length=64)


class User(UserBase):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    birth_day: Optional[date] = Field(default=None)


class Tweet(BaseModel):
    twwet_id: UUID = Field(...)
    content: str = Field(..., min_length=1, max_length=256)
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)

# Paths operations


@app.get(path="/")
def home():
    return {"titter api": "woriking!"}

# Users


@app.post(path="/signup", response_model=User, status_code=status.HTTP_201_CREATED, summary="Register a User", tags=["Users"])
def signup():
    pass


@app.post(path="/login", response_model=User, status_code=status.HTTP_200_OK, summary="Login a User", tags=["Users"])
def login():
    pass


@app.get(path="/users", response_model=List[User], status_code=status.HTTP_200_OK, summary="Show all users", tags=["Users"])
def show_users():
    pass


@app.get(path="/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK, summary="Show a User", tags=["Users"])
def show_user():
    pass


@app.delete(path="/users/{user_id}/delete", response_model=User, status_code=status.HTTP_200_OK, summary="Delete a User", tags=["Users"])
def delete_user():
    pass


@app.put(path="/users/{user_id}/update", response_model=User, status_code=status.HTTP_200_OK, summary="Update a User", tags=["Users"])
def update_user():
    pass


# Tweets
