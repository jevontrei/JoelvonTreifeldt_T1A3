from analysis import analyse_melody, process_likelihood, analyse_progression
from build_chords import build_triad, build_chord_scale
from build_scales import build_all_scales, build_penta
from formatting import format_input_notes, format_output_notes, format_input_chords, format_output_chords
import os

# os.system("clear")

# Initialise global variables; Define root note names, scale intervals and qualities:
roots = ["A_", "Bb", "B_", "C_", "Db", "D_",
         "Eb", "E_", "F_", "Gb", "G_", "Ab"]
major_scale_intervals = [0, 2, 4, 5, 7, 9, 11]
major_scale_qualities = ["maj", "min", "min", "maj", "maj", "min", "dim"]
all_keys = build_all_scales(roots, major_scale_intervals)
# print(f"All keys: {all_keys}")
# print(f"Root notes; {roots}")


def main():
    # try:

    print("Welcome! Let's play. What would you like to investigate?")
    print()
    print("1. Analyse a melody")
    print("2. Build a pentatonic scale")
    print("3. Find a specific chord within a key")
    print("4. Build a chord scale")
    print("5. Analyse a chord progression")
    print("6. Exit")
    print()

    while True:
        selection = int(input("Select an option between 1 and 6: ").strip(" "))
        # could also use match case instead here:
        
        if selection == 1:
            print()
            # Get input string and split it into a list
            melody_input = input(
                "Enter two or more notes separated by commas, e.g. Db, A, B, E (use flats, not sharps): ").split(",")
            # assert()
            # error handling: what if they enter e.g. a,b or Hsharp? print message except catch raise etc
            # print(f"Unformatted melody: {melody_input}")
            my_melody = format_input_notes(melody_input)
            # print(f"Formatted melody notes: {my_melody}")
            # print("---------------------------")
            most_likely_keys = analyse_melody(my_melody, all_keys)
            # print(f"Most likely key/s: {most_likely_keys}")
            # rename to formatted_output or something
            most_likely_keys = format_output_notes(most_likely_keys)
            # print(f"Re/un?formatted unprocessed most_likely_keys: {most_likely_keys}")
            result = process_likelihood(most_likely_keys)
            print(result)
            # also print compatible chords to accompany melody!!!!!!!
            print()
            # return ?

        elif selection == 2:
            print()
            request = input(
                "Enter a root note and a quality separated by a comma, e.g. 'E, min' or 'F, maj': ")
            try:
                request = request.split(",")
                tonic_input = format_input_notes(request[0])
                result = build_penta(tonic_input, roots,
                                     request[1].strip(" ").lower())
                if result != []:
                    print(result)
            except Exception as e:
                print(
                    f"Sorry, unexpected error: {e}. Please enter a valid input.")

        elif selection == 3:
            print()
            # triad_qualities = ["maj", "min", "dim"]  # add sus2, sus4
            # print(f"Triad qualities: {triad_qualities}")
            what_chord = input(
                "Now enter a scale and a degree between 1 and 7 (e.g. To find the 5th chord in the key of D, enter 'D, 5') separated by a comma: ").split(",")
            input_note = format_input_notes(what_chord[0])
            input_scale = all_keys[input_note]
            # print(f"Input scale: {input_scale}")
            input_degree = int(what_chord[1].strip(" "))
            name, chord = build_triad(
                input_scale, input_degree, major_scale_qualities)
            # now don't forget to unformat chord!!!
            # format_output_chords()
            print(
                f"In the key of {input_note}, chord {input_degree} is {name}: {chord}")
            print()
            # return ?

        elif selection == 4:
            print()
            which_chord_scale = input(
                "Cool! Okay please enter ONE root note (e.g. D, Ab, or B): ")
            which_chord_scale = format_input_notes(which_chord_scale)
            which_chord_scale = all_keys[which_chord_scale]

            chord_scale = build_chord_scale(
                which_chord_scale, major_scale_qualities)

            # print(chord_scale)
            # for p in chord_scale:
            #     for degree in range(1, 8):
            #         print(f"Chord {degree} is None: {chord_scale[p]}")

            # print(chord_scale.index(p))
            print()
            # triads = {}
           # return ?


        elif selection == 5:
            print()
            my_progression = input("Enter a progression of triads from a single key, separated by commas, e.g. 'Emin, Amin, Dmin, Gmaj'.\n(Hint: use the chord scale builder (option 4) if unsure of which chords fit together): ")
            result = analyse_progression(my_progression, all_keys)
            print(result)
            
            
        elif selection == 6:
            print()
            print("So long! Thanks for playing.")
            print()
            break
        
        
        
        else:
            print()
            print("Sorry, invalid! Please enter a number between 1 and 6.")
            
            
            
        # except Exception as e:
        #     print(f"Oops! Unexpected error: {e}")
        #     return ""


if __name__ == "__main__":
    main()
