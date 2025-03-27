from fastapi import FastAPI

from src.auth.router import router as auth_router
from src.pages.user_router import router as user_router_page


app = FastAPI()
app.include_router(auth_router)
app.include_router(user_router_page)

