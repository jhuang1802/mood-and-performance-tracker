import json
from fastapi import HTTPException
from models import Mood, MoodCreate

def read_json():
    with open("moods.json", "r") as file:
        return json.load(file)

def add_mood(new_data: MoodCreate):
    moods = read_json()
    if len(moods) == 0:
        next_id = 1
    else:
        next_id = max(mood["id"] for mood in moods) + 1

    new_mood = Mood(
        id = next_id,
        rating = new_data.rating,
        notes = new_data.notes,
    )

    moods.append(new_mood.model_dump(mode='json'))
    overwrite_moods(moods)
    return new_mood

def overwrite_moods(moods: list):
    with open("moods.json", "w") as file:
        json.dump(moods, file, indent=4)

def delete_mood(id: int):
    moods = read_json()
    mood, i = get_mood_and_index(id, moods)
    del moods[i]
    overwrite_moods(moods)
    return mood
    
def get_mood(id: int):
    moods = read_json()
    mood, _ = get_mood_and_index(id, moods)
    return mood

def update_mood(id: int, new_data: MoodCreate):
    moods = read_json()
    _, i = get_mood_and_index(id, moods)

    updated_mood = Mood(
        id = id,
        rating = new_data.rating,
        notes = new_data.notes
    )

    moods[i] = updated_mood.model_dump(mode="json")

    overwrite_moods(moods)
    return updated_mood

        
def get_mood_and_index(id: int, moods: list):
    if not moods:
        raise HTTPException(status_code=404, detail="Empty mood list")
    
    for i, mood in enumerate(moods):
        if mood["id"] == id:
            return mood, i

    raise HTTPException(status_code=404, detail="ID not found")