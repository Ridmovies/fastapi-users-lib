from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from src.auth.backend import auth_backend
from src.auth.models import User
from src.auth.schemas import UserRead, UserUpdate, UserCreate
from src.auth.user_manager import get_user_manager

router = APIRouter()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)


router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


current_user = fastapi_users.current_user()

