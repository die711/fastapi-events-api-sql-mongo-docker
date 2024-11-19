from fastapi import APIRouter, HTTPException, status
from models.inmemory.users import User, UserSignIn

user_router = APIRouter(
    tags=["User"]
)

users: dict[str, User] = {}


@user_router.post("/signup")
async def sign_user_up(user: User) -> dict:
    if user.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists"
        )

    users[user.email] = user
    return {
        "message": "User successfully registered"
    }


@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )

    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credential passed"
        )

    return {
        "message": "User signed in successfully"
    }
