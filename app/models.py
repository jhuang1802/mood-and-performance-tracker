from pydantic import BaseModel, Field

class MoodCreate(BaseModel):
    rating: int = Field(gt=0, lt=11)
    notes: str | None = None

class Mood(BaseModel):
    id: int
    rating: int = Field(gt=0, lt=11)
    notes: str | None = None