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


class UserRegister(User):
    password: str = Field(..., min_length=8, max_length=64)


class Tweet(BaseModel):
    twwet_id: UUID = Field(...)
    content: str = Field(..., min_length=1, max_length=256)
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)

# Paths operations

# Users


# Register a user
@app.post(path="/signup", response_model=User, status_code=status.HTTP_201_CREATED, summary="Register a User", tags=["Users"])
def signup():
    """
    Signup
    
    This path operation register a new user in the app

    Parameters:
        - Request body parameter
            - user: UserRegister

    Returns a json with the basic information
    """


# Login a user
@app.post(path="/login", response_model=User, status_code=status.HTTP_200_OK, summary="Login a User", tags=["Users"])
def login():
    pass


# Show all users
@app.get(path="/users", response_model=List[User], status_code=status.HTTP_200_OK, summary="Show all users", tags=["Users"])
def show_users():
    pass


# Show a user
@app.get(path="/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK, summary="Show a User", tags=["Users"])
def show_user():
    pass


# Delete a user
@app.delete(path="/users/{user_id}/delete", response_model=User, status_code=status.HTTP_200_OK, summary="Delete a User", tags=["Users"])
def delete_user():
    pass


# Update a user
@app.put(path="/users/{user_id}/update", response_model=User, status_code=status.HTTP_200_OK, summary="Update a User", tags=["Users"])
def update_user():
    pass


# Tweets


# Show all tweets
@app.get(path="/", response_model=List[Tweet], status_code=status.HTTP_200_OK, summary="Show all tweets", tags=["Tweets"])
def show_tweets():
    return {"titter api": "woriking!"}


# Post a tweet
@app.post(path="/post", response_model=Tweet, status_code=status.HTTP_201_CREATED, summary="Post a tweet", tags=["Tweets"])
def post():
    pass


# Show a tweet
@app.get(path="/tweets/{tweet_id}", response_model=Tweet, status_code=status.HTTP_200_OK, summary="Show a twee", tags=["Tweets"])
def show_tweet():
    pass


# Delete a tweet
@app.delete(path="/tweets/{tweet_id}/delete", response_model=Tweet, status_code=status.HTTP_200_OK, summary="Delete a tweet", tags=["Tweets"])
def delete_tweet():
    pass


# Update a tweet
@app.put(path="/tweets/{tweet_id}/update", response_model=Tweet, status_code=status.HTTP_200_OK, summary="Update a tweet", tags=["Tweets"])
def update_tweet():
    pass
