from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy

from src.auth.strategy import get_database_strategy
from src.auth.transport import bearer_transport

SECRET = "SECRET"


auth_backend = AuthenticationBackend(
    # name="jwt",
    # transport=bearer_transport,
    # get_strategy=get_jwt_strategy,
    name="access_token_db",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)