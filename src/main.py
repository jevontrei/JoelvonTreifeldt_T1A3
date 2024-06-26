from formatting import format_input, format_output
from builders import triad_builder, chord_scale_builder, build_all_scales
from analysis import key_analysis, process_likelihood
import os

os.system("clear")


def main():
    # try:
    print("Welcome! Let's play. What would you like to investigate?")
    print("1. Analyse a melody")
    print("2. Find a specific chord within a key")
    print("3. Build a chord scale")
    print("4. Exit")
    print()

    while True:
        selection = int(input("Select an option between 1 and 4: ").strip(" "))
        # could also use match case instead here:
        if selection == 1:
            analyse_melody()
            # return ?
        elif selection == 2:
            triad_builder()
            # return ?
        elif selection == 3:
            chord_scale_builder()
            # return ?
        elif selection == 4:
            print()
            print("So long!")
            print()
            break
        else:
            print("Sorry, invalid! Please enter a number between 1 and 3.")
    # except Exception as e:
    #     print(f"Oops! Unexpected error: {e}")
    #     return ""


if __name__ == "__main__":
    main()

# Define the 12 root note names
roots = ["A_", "Bb", "B_", "C_", "Db", "D_",
         "Eb", "E_", "F_", "Gb", "G_", "Ab"]
# print(f"Root notes; {roots}")

# Define major scale intervals
major_scale_intervals = [0, 2, 4, 5, 7, 9, 11]

# Define major scale qualities
major_scale_qualities = ["maj", "min", "min", "maj", "maj", "min", "dim"]

# Define pentatonic scale intervals
# major_scale_intervals = [0, 2, 4, 7, 9]

all_keys = build_all_scales(roots, major_scale_intervals)

# Get input string and split it into a list
melody_input = input(
    "Enter two or more notes separated by commas, e.g. Db, A, B, E (use flats, not sharps): ").split(",")
# assert()

# error handling: what if they enter e.g. a,b or Hsharp? print message except catch raise etc

# print(f"Unformatted melody: {melody_input}")

my_melody = format_input(melody_input)
# print(f"Formatted melody notes: {my_melody}")

# print("---------------------------")

most_likely_keys = key_analysis(my_melody, all_keys)
# print(f"Most likely key/s: {most_likely_keys}")

most_likely_keys = format_output(most_likely_keys)
# print(f"Re/un?formatted unprocessed most_likely_keys: {most_likely_keys}")

result = process_likelihood(most_likely_keys)
print(result)

# also print compatible chords to accompany melody!!!!!!!

print()
print("`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,")
print()

# triad_qualities = ["maj", "min", "dim"]  # add sus2, sus4
# print(f"Triad qualities: {triad_qualities}")

what_chord = input(
    "Now enter a scale and a degree between 1 and 7 (e.g. To find the 5th chord in the key of D, enter 'D, 5') separated by commas: ").split(",")
input_scale = all_keys[format_input(what_chord[0])]
# print(f"Input scale: {input_scale}")
input_degree = int(what_chord[1].strip(" "))
name, chord = triad_builder(input_scale, input_degree, major_scale_qualities)

# now don't forget to unformat chord!!!
print(f"{name}: {chord}")

print()
print("`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,")
print()

what_chord_scale = input(
    "Cool! Okay please enter ONE root note (e.g. D, Ab, or B): ")
chord_scale = chord_scale_builder(what_chord_scale)
print(chord_scale)

# triads = {}
