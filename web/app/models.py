from sqlalchemy import Column, Integer, LargeBinary, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), nullable=False)
    image = Column(LargeBinary, nullable=False)
