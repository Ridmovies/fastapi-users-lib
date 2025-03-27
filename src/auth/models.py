from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyBaseUserTableUUID
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


# class User(SQLAlchemyBaseUserTable[int], Base):
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass
