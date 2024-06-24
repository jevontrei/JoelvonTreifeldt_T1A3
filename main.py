import os
os.system("clear")

# Define the 12 root note names
roots = ["A_", "Bb", "B_", "C_", "Db", "D_",
         "Eb", "E_", "F_", "Gb", "G_", "Ab"]
# print(roots)
# Create a 2-octave list of root notes for scale and chord building
roots_doubled = roots * 2
# print(roots_doubled)

# The scale_builder (function?) takes a root note as input and constructs a major scale on that note
# Define blueprint for major scale intervals
major_scale = [0, 2, 4, 5, 7, 9, 11]
keys = []
# def scale_builder(root,):
for i in range(12):
    key = []
    for k in major_scale:
        key.append(roots_doubled[i + k])
#     print(key)
    keys.append(key)
# return ...
# print(keys)

all_keys = dict(zip(roots, keys))
# print(all_keys)


# for scale in all_keys:
#         print(scale)

# keys = {"A": }
# return ...

# triads = {}

melody = input(
    "Enter two or more notes separated by commas, e.g. A, Db, B, E (use flats, not sharps): ").upper()
# Break input string into a list and clean commas and space characters
melody = melody.split(",")
for i in range(len(melody)):
    melody[i] = melody[i].strip(" ")
# print(f"Melody: {melody}")

# error handling: what if they enter e.g. a,b or Hsharp? print message except catch raise etc

for i in range(len(melody)):
    if len(melody[i]) == 2:
        melody[i] = melody[i][0].upper() + melody[i][1].lower()
    elif len(melody[i]) == 1:
        melody[i] += "_"
    else:
        print("Error. Please enter note names with 1 or 2 characters")
        
# Store melody notes in a set to remove duplicate values
melody = set(melody)

print(f"Melody: {melody}")


key_analysis = []
for note in melody:
    for scale in all_keys:
        if note in all_keys[scale]:
            key_analysis.append(scale)
        else:
            print("Sorry, note not found.")
            key_analysis = []
            break
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

# for key in most_likely_key:
#         if "_" in key:
#                 key = key[:-1]

if len(most_likely_key) > 0:
    print(
        f"Most likely key/s: {most_likely_key} with confidence {1 / len(most_likely_key)}.")  # print out a list of 
else:
    print("Error! Please enter valid note names.")
# print(max(confidence))


# triad_qualities = ["maj", "min", "dim"]  # add sus2, sus4
# print(f"Triad qualities: {triad_qualities}")
