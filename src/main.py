from analysis import analyse_melody, process_likelihood, analyse_progression
from build_chords import build_triad, build_chord_scale
from build_scales import build_all_scales, build_penta
from formatting import format_input_notes, format_output_notes, format_input_chords, format_output_chords
import os

os.system("clear")

# Initialise global variables; Define root note names, scale intervals, scale qualities, and keys:
roots = ["A_", "Bb", "B_", "C_", "Db", "D_",
         "Eb", "E_", "F_", "Gb", "G_", "Ab"]
major_scale_intervals = [0, 2, 4, 5, 7, 9, 11]
major_scale_qualities = ["maj", "min", "min", "maj", "maj", "min", "dim"]
all_keys = build_all_scales(roots, major_scale_intervals)


# This main function ...

def main():
    """_summary_

    Returns:
        _type_: _description_
    """

    try:
        while True:

            print()
            print("`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,")
            print()
            print("Welcome! Let's play. What would you like to investigate?")
            print()
            print("1. Analyse a melody")
            print("2. Build a pentatonic scale")
            print("3. Find a specific chord within a key")
            print("4. Build a chord scale")
            print("5. Analyse a chord progression")
            print("6. Exit")
            print()

            selection = int(
                input("Select an option between 1 and 6: ").strip(" "))

            if selection == 1:
                print()

                # Get input string and split it into a list:
                melody_input = input(
                    "Enter two or more notes separated by commas, e.g. Db, A, B, E (use flats, not sharps): ").split(",")

                # assert()
                # error handling: what if they enter e.g. a,b or Hsharp? print message except catch raise etc

                my_melody = format_input_notes(melody_input)

                most_likely_keys = analyse_melody(my_melody, all_keys)

                # rename to formatted_output or something
                most_likely_keys = format_output_notes(most_likely_keys)
                result = process_likelihood(most_likely_keys)

                print(result)
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

                what_chord = input(
                    "Now enter a scale and a degree between 1 and 7 (e.g. To find the 5th chord in the key of D, enter 'D, 5') separated by a comma: ").split(",")

                input_note = format_input_notes(what_chord[0])
                input_scale = all_keys[input_note]
                input_degree = int(what_chord[1].strip(" "))
                name, chord = build_triad(
                    input_scale, input_degree, major_scale_qualities)

                # now don't forget to unformat chord!!!
                # format_output_chords()

                print(
                    f"In the key of {input_note}, chord {input_degree} is {name}: {chord}.")

                # return ?

            elif selection == 4:
                print()
                which_chord_scale = input(
                    "Cool! Okay please enter ONE root note (e.g. D, Ab, or B): ")

                which_chord_scale = format_input_notes(which_chord_scale)
                which_chord_scale = all_keys[which_chord_scale]

                chord_scale, chord_names = build_chord_scale(
                    which_chord_scale, major_scale_qualities)

            # return ?

            elif selection == 5:
                print()

                my_progression = input(
                    "Enter a progression of triads from a single key, separated by commas, e.g. 'Emin, Amin, Dmin, Gmaj'.\n(Hint: use the chord scale builder (option 4) if unsure of which chords fit together): ").lower()

                result = analyse_progression(
                    my_progression, all_keys, major_scale_qualities)

                print(
                    f"These chord/s fit within the key/s of {result}.")

            elif selection == 6:
                print()
                print("So long! Thanks for playing.")
                print()
                break

            else:
                print()
                print("Sorry, invalid! Please enter a number between 1 and 6.")

    except Exception as e:
        print(f"Oops! Unexpected error: {e}.")
        return ""


# Ensure ...
if __name__ == "__main__":
    main()
