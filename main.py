from formatting import format_input, format_output
from builders import triad_builder, chord_scale_builder
import os
os.system("clear")

# Define the 12 root note names
roots = ["A_", "Bb", "B_", "C_", "Db", "D_",
         "Eb", "E_", "F_", "Gb", "G_", "Ab"]
roots_enharmonic = ["A_", "A#", "B_", "C_", "C#", "D_",
                    "D#", "E_", "F_", "F#", "G_", "G#"]
# print(f"Root notes; {roots}")
# print(f"Enharmonic root notes: {roots_enharmonic}")
# Create a 2-octave list of root notes for scale and chord building
roots_doubled = roots * 2
# print(roots_doubled)
roots_enharmonic_doubled = roots * 2
# print(roots_enharmonic_doubled)

# The scale_builder (function?) takes a root note as input and constructs a major scale on that note
# Define blueprint for major scale intervals
major_scale = [0, 2, 4, 5, 7, 9, 11]
keys = []
# def scale_builder(root,):
for i in range(12):
    key = []
    for k in major_scale:
        key.append(roots_doubled[i + k])
#     print(f"Key: {key}")
    keys.append(key)
# return ...
# print(f"Keys: {keys}")

all_keys = dict(zip(roots, keys))
# print(f"All keys: {all_keys}")


# for scale in all_keys:
#         print(scale)

# keys = {"A": }
# return ...

# triads = {}

melody = input(
    "Enter two or more notes separated by commas, e.g. A, Db, B, E (use flats, not sharps): ").split(",")
# .upper()

# error handling: what if they enter e.g. a,b or Hsharp? print message except catch raise etc


# put this in input/output cleaning/formatting function/module
# Break input string into a list and clean commas and space characters
# melody = melody.split(",")

# print(f"Unformatted melody: {melody}")


melody = format_input(melody)
# print(f"Formatted melody: {melody}")

# move this to the module function
# Store melody notes in a set to remove duplicate values
melody = set(melody)
# print(f"Melody notes: {melody}")
# print("---------------------------")

key_analysis = []
for note in melody:
    # print(f"Melody note: {note}")
    for scale in all_keys:
        # print(f"Scale: {scale}")
        # print(f"Scale: {all_keys[scale]}")
        if note in all_keys[scale]:
            key_analysis.append(scale)
            # print(f"Key analysis: {key_analysis}")
            # print("---------------------------")
        # else:
        #     print("Sorry, note not found.")
        #     print("---------------------------")
        #     key_analysis = []
        #     break
        #     print(f"Melody fits within the key of {scale}.")
        #     print("This melody combines multiple scales.")
# print(f"Key analysis: {key_analysis}")

confidence = {}
for key in key_analysis:
    occurrence = key_analysis.count(key)
    confidence[key] = round(occurrence / len(key_analysis), 2)
# print(f"Confidence: {confidence}")

max_conf = 0
most_likely_key = []
for key in confidence:
    if confidence[key] > max_conf:
        max_conf = confidence[key]
        most_likely_key = [key]
    elif confidence[key] == max_conf:
        most_likely_key.append(key)

# put this in input/output cleaning function / module
# print(f"Most likely key/s: {most_likely_key}")


def format_output(most_likely_key):
    # try:  # unnecessary bc i've already cleaned it all up in .input_formatting?
    # except:
    # catch:
    # raise:
    for key in range(len(most_likely_key)):
        if most_likely_key[key][-1] == "_":
            most_likely_key[key] = most_likely_key[key][0]
    return most_likely_key


most_likely_key = format_output(most_likely_key)
# print(f"Un?formatted most_likely_key: {most_likely_key}")

# make this a function and move this to a module:
if len(most_likely_key) > 0:
    likelihood = round(1 / len(most_likely_key), 2)
    if likelihood < 0.25:
        print(
            f"Oof, that's a spicy (or vague) melody! This result won't be very useful! But no shade thrown...\nHere are some potentially compatible keys anyway: {most_likely_key}, each with likelihood {likelihood}.")
    else:
        print(
            f"Most likely key/s: {most_likely_key}, each with likelihood {likelihood}.")  # print out a list of
else:
    print("Error! Please enter valid note names.")

# print(max(confidence))


# triad_qualities = ["maj", "min", "dim"]  # add sus2, sus4
# print(f"Triad qualities: {triad_qualities}")

print("`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,")

what_chord = input(
    "Enter a scale and a degree between 1 and 7 (e.g. To find the 5th chord in the key of D, enter 'D, 5') separated by commas: ").split(",")
input_scale = all_keys[format_input(what_chord[0])]
# print(f"Input scale: {input_scale}")
input_degree = int(what_chord[1].strip(" "))
chord = triad_builder(input_scale, input_degree)
# now unformat chord
print(chord)

print("`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,`-,")

what_chord_scale = input("Enter ONE root note (e.g. D, Ab, or B): ")
chord_scale = chord_scale_builder(what_chord_scale)
print(chord_scale)
