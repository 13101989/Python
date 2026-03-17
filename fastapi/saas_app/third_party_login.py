import httpx
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2
from sqlalchemy.orm import Session
from db_connection import get_session
from models import User
from operations import get_user


GITHUB_CLIENT_ID = "Ov23liJRxjYObCuIdAyA"
GITHUB_CLIENT_SECRET = "18231a4d3d6808fc281c0a162a6f2ee172d54ae4"
GITHUB_REDIRECT_URI = "http://localhost:8000/github/auth/token"
GITHUB_AUTHORIZATION_URL = "https://github.com/login/oauth/authorize"


def resolve_github_token(
    access_token: str = Depends(OAuth2()), session: Session = Depends(get_session)
) -> User:
    user_response = httpx.get(
        "https://api.github.com/user",
        headers={"Authorization": f"{access_token}"},
    ).json()
    username = user_response.get("login", " ")
    user = get_user(session, username)

    if not user:
        email = user_response.get("email", " ")
        user = get_user(session, email)

    if not user:
        raise HTTPException(status_code=403, detail="Token not valid")

    return user
