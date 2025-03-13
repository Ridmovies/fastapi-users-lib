from fastapi import FastAPI, Depends

from src.auth.auth_router import current_user, auth_router
from src.database import User

app = FastAPI()
app.include_router(auth_router)

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"