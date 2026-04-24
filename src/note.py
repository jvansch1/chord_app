import random

from constants import ACCIDENTAL, NATURAL, NOTE_NAMES, VALID_CHORD_NAMES, SHARP, FLAT, A, B, C, D, E, F, G, DOUBLE_SHARP, DOUBLE_FLAT

class Note:
    def __init__(self, name: str, accidental: ACCIDENTAL):
        self.name = name.upper()
        self.accidental = accidental


    @staticmethod
    def random_note():
        chord_letter = random.choice(NOTE_NAMES)
        accidental = random.choice(VALID_CHORD_NAMES[chord_letter])

        return Note(chord_letter, accidental)


    def __str__(self):
        letter = self.name

        if self.accidental == NATURAL:
            return letter

        return f"{letter}-{self.accidental}"

    
    def __eq__(self, other: object): 
        if not isinstance(other, Note):
            return False

        return self.name == other.name and self.accidental == other.accidental
    

    def is_valid_note(self) -> bool:
        note_found = False
        for enharmonic_equivalents in CHROMATIC_SCALE:
            if self in enharmonic_equivalents:
                note_found = True

        return note_found

    

CHROMATIC_SCALE: list[list[Note]] = [
    [Note(C, NATURAL), Note(B, SHARP), Note(D, DOUBLE_FLAT)],
    [Note(C, SHARP), Note(D, FLAT), Note(B, DOUBLE_SHARP)],
    [Note(D, NATURAL), Note(C, DOUBLE_SHARP), Note(E, DOUBLE_FLAT)],
    [Note(D, SHARP), Note(E, FLAT), Note(F, DOUBLE_FLAT)],
    [Note(E, NATURAL), Note(D, DOUBLE_SHARP), Note(F, FLAT)],
    [Note(F, NATURAL), Note(E, SHARP), Note(G, DOUBLE_FLAT)],
    [Note(F, SHARP), Note(G, FLAT), Note(E, DOUBLE_SHARP)],
    [Note(G, NATURAL), Note(F, DOUBLE_SHARP), Note(A, DOUBLE_FLAT)],
    [Note(G, SHARP), Note(A, FLAT)],
    [Note(A, NATURAL), Note(G, DOUBLE_SHARP), Note(B, DOUBLE_FLAT)],
    [Note(A, SHARP), Note(B, FLAT), Note(C, DOUBLE_FLAT)],
    [Note(B, NATURAL), Note(C, FLAT), Note(A, DOUBLE_SHARP)],
]