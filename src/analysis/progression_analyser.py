from formatting.input_formatting import format_input_notes
from build_chords.chord_scale_builder import build_chord_scale
import os


def analyse_progression(input_progression, key_centers, qualities):
    print()
    input_progression = input_progression.split(",")
    # Formatting:
    # use format chord module instead of this?:
    for i in range(len(input_progression)):
        input_progression[i] = input_progression[i].strip(" ")
        if input_progression[i][-3:] == "maj":
            input_progression[i] = format_input_notes(
                input_progression[i][:-3]) + "maj"
        elif input_progression[i][-3:] == "min":
            input_progression[i] = format_input_notes(
                input_progression[i][:-3]) + "min"
        else:
            print("Hmmmm please enter valid chords.")
            return ""
    print(f"input_progression: {input_progression}")


#
#
#
#
#
#
#
#
#
#
#
#
#

    # MOVE TESE INSIDE LOOOOP?
    pre_candidates = []
    post_candidates = []


#
#
#
#
#
#
#
#
#
#
#
#
#

    # fix this:
    for chord in input_progression:
        print(f"chord: {chord}")

        for key_center in key_centers.keys():
            print(f"key_center: {key_center}, {type(key_center)}")
            # print(f"qualities: {qualities}, {type(qualities)}")

            chord_scale, chord_names = build_chord_scale(
                key_centers[key_center], qualities)
            # print(f"chord_scale: {chord_scale}")
            print(f"chord_names: {chord_names}")
            if chord in chord_names:
                if pre_candidates == []:
                    pre_candidates.append(key_center)
                    print(f"pre_candidates: {pre_candidates}")
                elif pre_candidates != []:
                    # for i in pre_candidates:
                    # if i in key_centers[key_center]:
                    post_candidates.append(key_center)
                    # print(f"post_candidates: {post_candidates}")
            else:
                # ???:
                pass

            print(f"pre_candidates: {pre_candidates}")
            print(f"post_candidates: {post_candidates}")
            candidates = []
            for i in pre_candidates:
                if i in post_candidates:
                    candidates.append(i)
                    print(f"candidates: {candidates}")
            # print(f"key_centers[key_center]: {key_centers[key_center]}")
            # if chord in key_centers[key_center]:
            #     candidates.append(chord)
            #     print(f"candidates: {candidates}")
        print("--------------------")
        print()
    # os.system("clear")
    # print(f"candidates: {candidates}")
    return candidates
