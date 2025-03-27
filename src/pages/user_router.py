from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/test", tags=["page_users"])
templates = Jinja2Templates(directory="src/pages/templates")


@router.get("")
async def get_simple_page(request: Request):
    return templates.TemplateResponse(
        name="users/simple.html",
        context={"request": request},
    )

@router.get("/login")
async def get_login_page(request: Request):
    return templates.TemplateResponse(
        name="users/login.html",
        context={"request": request},
    )


@router.get("/register")
async def get_register_page(request: Request):
    return templates.TemplateResponse(
        name="users/register.html",
        context={"request": request},
    )
