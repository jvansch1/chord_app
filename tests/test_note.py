from note import Note
from constants import FLAT, NATURAL, SHARP

def test_natural_note_displays_correctly():
    note = Note('A', NATURAL)

    assert str(note) == 'A'


def test_flat_note_displays_correctly():
    note = Note('A', FLAT)

    assert str(note) == 'A-flat'


def test_sharp_note_displays_correctly():
    note = Note('C', SHARP)

    assert str(note) == 'C-sharp'