from pydantic import BaseModel

class SongBase(BaseModel):
    title: str
    author: str
    lyrics: str
    style: str
    file_path: str
    image_path: str

class SongCreate(SongBase):
    pass

class Song(SongBase):
    id: int

    class Config:
        orm_mode = True
