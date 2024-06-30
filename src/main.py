# Import internal and external modules/packages:
from analysis import analyse_melody, analyse_progression
from build_chords import build_triad, build_chord_scale
from build_scales import build_all_scales, build_penta
from formatting import format_input_notes, format_output_notes, format_input_chords, format_output_chords
import os

# Clear the terminal:
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

    # Loop over the main() function / user input prompt "while True" until a return statement is encountered:
    while True:
        try:
            # Display welcome message:
            print()
            print()
            print("`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,")
            print()
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

            # Ask user to choose an activity:
            selection = int(
                input("Select an option between 1 and 6: ").strip(" "))

            os.system("clear")

            if selection == 1:
                print()
                
                # Display legal inputs:
                print("Valid note names:")
                for i in roots:
                    print(f"> {i}")
                    
                print()

                # Get input melody string and split it into a list:
                melody_input = input(
                    "Enter two or more notes separated by commas, e.g. Db, A, B, E (use flats, not sharps)...\nIf you're not sure: try building a pentatonic scale (option 2) and using some of those notes! They work together well: ").split(",")

                os.system("clear")

                # Advise user that a one-note melody won't produce a very meaningful result:
                if len(melody_input) < 2:
                    print()
                    print(">>> Pssst! The result will be more meaningful if you enter more than one note! :')")

                # assert()

                # Format input list text for compatibility with the  "roots" and "all_keys" variables:
                my_melody = format_input_notes(melody_input)

                print()
                
                # Display formatted input:
                print(f">>> Input melody:\n{my_melody}")

                # Call melody analyser module:
                compatible_keys = format_output_notes(
                    analyse_melody(my_melody, all_keys))

                # Advise user that nothing meaningful was found:
                if compatible_keys == []:
                    print(">>> Sorry, we couldn't narrow that spicy (or invalid) melody down to one key. Future versions of this program will be able to handle more complex melodies! Please enter a valid melody, or simplify your melody.")
                    
                else:
                    print(f">>> Compatible keys: {compatible_keys}.")

                # return ?

            elif selection == 2:
                print()
                
                # Get pentatonic scale name from user and split it into a list:
                request = input(
                    "Enter a root note and a quality separated by a comma, e.g. 'E, min' or 'F, maj': ").split(",")

                # !Am i doubling up try/except blocks? it's here AND also in the module :S ... HOWEVER for some reason if i delete the main try/except block and just use the inner/module one, when it fails it doesn't go back to prompting user for input. why?
                # try:

                print()
                print(f">>> Input: {request}")

                tonic_input = format_input_notes(request[0])
                quality_input = request[1].strip(" ").lower()

                if len(request) != 2 or len(tonic_input) != 2 or len(quality_input) != 3:
                    print(">>> Sorry, invalid input. Please try again.")
                    continue

                result = build_penta(tonic_input, roots,
                                     quality_input)

                if result != []:
                    print(
                        f">>> Your pentatonic scale is {result}.")

                # except Exception as e:
                #     print()
                #     print(
                #         f"__main__ Sorry, unexpected error: {e}. Please enter a valid input.")

            elif selection == 3:
                print()

                what_chord = input(
                    "Now enter a scale and a degree between 1 and 7 (e.g. To find the 5th chord in the key of D, enter 'D, 5') separated by a comma: ").split(",")

                print()
                print(f">>> Input: {what_chord}")

                input_note = format_input_notes(what_chord[0])

                if input_note not in all_keys.keys():
                    print(">>> Sorry, invalid input. Please try again.")
                    continue

                input_scale = all_keys[input_note]
                input_degree = int(what_chord[1].strip(" "))
                name, chord = build_triad(
                    input_scale, input_degree, major_scale_qualities)

                # now don't forget to unformat chord!!!
                # format_output_chords()

                print(
                    f">>> In the key of {input_note}, chord {input_degree} is {name}: {chord}.")

                # return ?

            elif selection == 4:
                print()
                which_chord_scale = input(
                    "Cool! Okay please enter ONE root note (e.g. D, Ab, or B): ")

                print()
                print(f">>> Input: {which_chord_scale}")

                which_chord_scale = format_input_notes(which_chord_scale)

                if which_chord_scale not in all_keys.keys():
                    print(">>> Sorry, invalid input. Please try again.")
                    continue

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

                if len(result) == 0:
                    print()
                    print(">>> Sorry! No result to display. Either the input is invalid or these chords don't fit within one key. Future version of this app will be able to help you with more spicy progressions!")

                else:
                    print(
                        f">>> These chord/s fit within the key/s of {result}.")

            elif selection == 6:
                print()
                print(">>> So long! Thanks for playing.")
                print()
                return

            else:
                print()
                print(">>> Sorry, invalid! Please enter a number between 1 and 6.")

        except Exception as e:
            print()
            os.system("clear")
            print()
            print(
                f"__main__ >>> Oops! Unexpected error: {e}. Please try again with a valid input.")


# Ensure ... :
if __name__ == "__main__":
    main()
