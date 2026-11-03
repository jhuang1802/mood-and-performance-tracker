from fastapi import HTTPException
from models import Mood, MoodCreate
import database

def get_all_moods():
    response = database.get_all_moods()
    result = []

    for mood in response:
        result.append(dict(mood))
    return result

def get_mood(id: int):
    response = database.get_mood(id)
    return dict(response)

def add_mood(new_data: MoodCreate):
    response = database.add_mood(new_data.rating, new_data.notes)
    return dict(response)

def delete_mood(id: int):
    response = database.delete_mood(id)
    return dict(response)

def replace_mood(id: int, new_data: MoodCreate):
    response = database.replace_mood(id, new_data.rating, new_data.notes)
    return dict(response)