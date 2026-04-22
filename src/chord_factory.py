import random

from note import Note
from constants import MAJOR, CHORD_QUALITIES
from major_chord import MajorChord
from minor_chord import MinorChord


def chord_factory(note: Note):
    random_chord_quality = random.choice(CHORD_QUALITIES)
    if random_chord_quality == MAJOR:
        return MajorChord(note, random_chord_quality)
    else:
        return MinorChord(note, random_chord_quality)