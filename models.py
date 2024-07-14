# models.py

from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    answer = Column(String)
    user_id = Column(Integer)
    created_at = Column(TIMESTAMP)
    question = Column(String)
