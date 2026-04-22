from constants import ACCIDENTALS
from constants import ACCIDENTAL
from constants import NOTE_NAMES, NATURAL
from note import Note

def get_note_from_answer(input_note: str):
    note = input_note.strip()

    if len(note) == 1:
        if note.upper() not in NOTE_NAMES:
            raise ValueError("Not a valid note name")

        return Note(note, NATURAL)

    elif len(note) > 1:
        note_name, accidental_str = note.split("-")

        note_name = note_name.strip().upper()
        accidental: ACCIDENTAL = parse_accidental(accidental_str)
        new_note = Note(note_name, accidental)

        if not new_note.is_valid_note():
            raise ValueError("Not a valid note Name")

        return new_note

    raise ValueError("Empty input")


def parse_accidental(value: str) -> ACCIDENTAL:
    formatted_value = value.lower()
    if formatted_value not in ACCIDENTALS:
        raise ValueError(f"Invalid Accidental: {value}")

    # pyrefly: ignore[bad-return]
    return formatted_value
          


def validate_answer(answer: list[str]):
    if len(answer) != 3:
        raise ValueError("Error should be a comma separated list of values")

    # Now we need to check if each note is actually something real
    # There are 2 cases here:
    # 1. Just a note name like A
    #     Here we can upcase the letter and compare it
    # 2. We get something like D-Flat or F-sharp
    #     Here we should split on "-" validate the letter name, as well as the accidental

    validated_notes = [get_note_from_answer(note) for note in answer]
    return validated_notes


def parse_answer(answer: str) -> list[Note]:
    split_answer = answer.split(",")
    return validate_answer(split_answer)
