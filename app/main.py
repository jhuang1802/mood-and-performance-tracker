from fastapi import FastAPI
from models import MoodCreate
import storage

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, Jimmy!"}

@app.get("/moods")
def get_moods():
    return storage.read_json()

@app.post("/moods")
def add_mood(mood: MoodCreate):
    return storage.add_mood(mood)
    
@app.delete("/moods/{id}")
def delete_mood(id: int):
    return storage.delete_mood(id)
        
@app.get("/moods/{id}")
def get_mood(id: int):
    return storage.get_mood(id)    

@app.put("/moods/{id}")
def update_mood(id: int, mood: MoodCreate):
    return storage.update_mood(id, mood)