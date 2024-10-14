from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserModel(Base):
    __tablename__ = "Users"

    UserId = Column(Integer, primary_key=True, index=True)
    Name = Column(String(50), nullable=False)
    Email = Column(String(100), nullable=False, unique=True)
    Location = Column(String(100), nullable=False)
    Company = Column(String(100), nullable=False)
