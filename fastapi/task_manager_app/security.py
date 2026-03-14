from pydantic import BaseModel
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Optional

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "hashed_password": "hashedsecret",
    },
    "janedoe": {
        "username": "janedoe",
        "hashed_password": "hashedsecret2",
    },
}


def fakely_hash_password(password: str) -> str:
    return f"hashed{password}"


class User(BaseModel):
    username: str


class UserInDb(User):
    hashed_password: str


def get_user(db, username: str) -> Optional[UserInDb]:
    if username in db:
        user_dict = db[username]
        return UserInDb(**user_dict)


def fake_token_generator(user: UserInDb) -> str:
    return f"tokenized{user.username}"


def fake_token_resolver(token: str) -> Optional[UserInDb]:
    if token.startswith("tokenized"):
        user_id = token.removeprefix("tokenized")
        user = get_user(fake_users_db, user_id)
        return user


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_user_from_token(token: str = Depends(oauth2_scheme)) -> UserInDb:
    user = fake_token_resolver(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
