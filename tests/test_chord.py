from constants import DOUBLE_FLAT
from minor_chord import MinorChord
from constants import NOTE_NAMES
from major_chord import MajorChord
from constants import NATURAL
from constants import SHARP
from constants import FLAT, MAJOR, MINOR
from chord import Chord
from note import Note

def test_major_chord_with_flat_displays_correctly():
    note = Note('A', FLAT)
    chord = Chord(note, MAJOR)

    assert str(chord) == "A-flat Major"


def test_minor_chord_with_flat_displays_correctly():
    note = Note('A', FLAT)
    chord = Chord(note, MINOR)

    assert str(chord) == "A-flat Minor"


def test_major_chord_with_sharp_displays_correctly():
    note = Note('C', SHARP)
    chord = Chord(note, MAJOR)

    assert str(chord) == "C-sharp Major"


def test_minor_chord_with_sharp_displays_correctly():
    note = Note('C', SHARP)
    chord = Chord(note, MINOR)

    assert str(chord) == "C-sharp Minor"


def test_natural_major_chord():
    note = Note('C', NATURAL)
    chord = Chord(note, MAJOR)

    assert str(chord) == "C Major"


def test_natural_minor_chord():
    note = Note('C', NATURAL)
    chord = Chord(note, MINOR)

    assert str(chord) == "C Minor"


## Assert the logic of getting the chord tones

def test_gets_chord_names_with_no_accidentals():
    note = Note('C', NATURAL)
    chord = MajorChord(note, MAJOR)

    expected_chord_tones = chord.get_note_names()

    assert note in expected_chord_tones
    assert Note('E', NATURAL) in expected_chord_tones
    assert Note('G', NATURAL) in expected_chord_tones


def test_gets_chord_names_with_sharps():
    note = Note("F", SHARP)
    chord = MajorChord(note, MAJOR)

    expected_chord_tones = chord.get_note_names()

    assert note in expected_chord_tones
    assert Note("A", SHARP) in expected_chord_tones
    assert Note("C", SHARP) in expected_chord_tones


def test_gets_chord_with_double_flat():
    note = Note('G', FLAT)
    chord = MinorChord(note, MINOR)

    expected_chord_tones = chord.get_note_names()
    assert note in expected_chord_tones
    assert Note('B', DOUBLE_FLAT) in expected_chord_tones
    assert Note('D', FLAT) in expected_chord_tones
