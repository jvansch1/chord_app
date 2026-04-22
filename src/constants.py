from typing import Literal

LETTER = Literal['A', 'B', 'C', 'D', 'E', 'F', 'G']

## Letter names
A: LETTER = 'A'
B: LETTER = 'B'
C: LETTER = 'C'
D: LETTER = 'D'
E: LETTER = 'E'
F: LETTER = 'F'
G: LETTER = 'G'

ACCIDENTAL = Literal['natural', 'sharp', 'flat', 'doublesharp', 'doubleflat']

## Accidentals
NATURAL: ACCIDENTAL = 'natural'
SHARP: ACCIDENTAL = 'sharp'
FLAT: ACCIDENTAL = 'flat'
DOUBLE_SHARP: ACCIDENTAL = 'doublesharp'
DOUBLE_FLAT: ACCIDENTAL = 'doubleflat'


## Chord qualities
MAJOR = 'Major'
MINOR = 'Minor'

NOTE_NAMES: list[str] = [
    A, B, C, D, E, F, G
]

ACCIDENTALS: list[ACCIDENTAL] = [SHARP, FLAT, DOUBLE_FLAT, DOUBLE_SHARP]

VALID_CHORD_NAMES: dict[str, list[ACCIDENTAL]] = {
    A: [NATURAL, FLAT],
    B: [NATURAL, FLAT],
    C: [NATURAL, SHARP, FLAT],
    D: [NATURAL, FLAT],
    E: [NATURAL, FLAT],
    F: [NATURAL, SHARP],
    G: [NATURAL, FLAT]
}

CHORD_QUALITIES: list[str] = [MAJOR, MINOR]

CHORD_TO_NOTES = {
    'C Major': [C, E, G]
}
