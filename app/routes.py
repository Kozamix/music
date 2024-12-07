from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from . import crud, database, models
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(database.get_db)):
    songs = crud.get_songs(db)
    return templates.TemplateResponse("index.html", {"request": request, "songs": songs})

@router.get("/song/{song_id}", response_class=HTMLResponse)
def song_page(song_id: int, request: Request, db: Session = Depends(database.get_db)):
    song = crud.get_song(db, song_id)
    if song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return templates.TemplateResponse("song.html", {"request": request, "song": song})
