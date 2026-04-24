from fastapi import FastAPI

from chord_factory import chord_factory
from note import Note

app = FastAPI()


@app.get("/")
def get_chord():
    random_note = Note.random_note()
    chord = chord_factory(random_note)
    return {
        "chord": str(chord),
        "chord_notes": chord.get_note_names()
    }
