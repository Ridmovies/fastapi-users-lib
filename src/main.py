from fastapi import FastAPI, Depends

from src.auth.router import router as auth_router, current_user
from src.auth.models import User

app = FastAPI()
app.include_router(auth_router)

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"