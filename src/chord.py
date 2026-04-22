from constants import NOTE_NAMES
from abc import abstractmethod

from constants import FLAT
from note import Note, CHROMATIC_SCALE


class Chord:
    def __init__(self, root: Note, quality: str):
        self._root = root
        self._quality = quality

    @property
    @abstractmethod
    def FORMULA(self) -> list[int]:
        pass


    @property
    def root(self):
        return str(self._root)


    @property
    def quality(self):
        return self._quality


    def __str__(self):
        return self.root + ' ' + self.quality


    ## The logic here is still not quite right
    ## Right now we don't handle cases where we have double sharps or flats
    ## For example, for a G-flat minor chord we are getting those notes
    ## g-flat, a, d-flat
    ## Technically these are the right notes but it should be notated as g-flat, b-doubleflat, d-flat
    def get_note_names(self):
        ## We are going to start with the root note, and collect all the extended notes by
        ## iterating through the chromatic scale and getting those noses
        # Lets first get the letter names.
        chord_letter_names = []

        index = NOTE_NAMES.index(self._root.name)

        for i in range(2):
            index += 2
            index %= len(NOTE_NAMES)
            chord_letter_names.append(NOTE_NAMES[index])

        all_chord_notes = [self._root]

        current_index = 0
        letter_name_index = 0

        print(f"all chord notes: {all_chord_notes}")
        print()

        for index, enharmonic_equivalents in enumerate(CHROMATIC_SCALE):
            if self._root in enharmonic_equivalents:
                current_index = index

        for index_change in self.FORMULA:
            current_index = (current_index + index_change) % len(CHROMATIC_SCALE)

            next_letter = chord_letter_names[letter_name_index]
            enharmonic_equivalents = CHROMATIC_SCALE[current_index]

            for note in enharmonic_equivalents:
                if note.name == next_letter:
                    all_chord_notes.append(note)

            letter_name_index += 1


        return all_chord_notes

    