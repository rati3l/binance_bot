from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Next_Operation(Base):
    __tablename__ = 'operation'
    id = Column(Integer, primary_key=True)
    value = Column(String)

class Score(Base):
    __tablename__ = 'score'
    id = Column(Integer, primary_key=True)
    value = Column(Integer)
