from sqlalchemy import Column, Integer, String
from .database import Base

class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    lyrics = Column(String)
    style = Column(String)
    file_path = Column(String)
    image_path = Column(String)
