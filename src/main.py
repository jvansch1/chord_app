from chord_factory import chord_factory
from note import Note

from answer_parser import parse_answer
from chord import Chord

    
        
def check_answer(chord: Chord, notes: list[Note]):
    expected_note_names = chord.get_note_names()

    for note in expected_note_names:
        if note not in notes:
            print("Not Correct")
            return

    print("Correct!")


if __name__ == "__main__":
    random_note = Note.random_note()
    chord = chord_factory(random_note)
    answer = input(f"{str(chord)}\n")
    individual_note_names = parse_answer(answer)

    check_answer(chord, individual_note_names)



    
        




