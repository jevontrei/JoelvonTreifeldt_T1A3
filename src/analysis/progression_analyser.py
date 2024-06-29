from formatting.input_formatting import format_input_notes
from build_chords.chord_scale_builder import build_chord_scale
import os


def analyse_progression(input_progression, key_centers, qualities):
    """_summary_

    Args:
        input_progression (_type_): _description_
        key_centers (_type_): _description_
        qualities (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        print()
        input_progression = input_progression.split(",")

        # Formatting: use format chord module instead of this?:
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

        # Initialise sets for candidate keys:
        pre_candidates = set()
        post_candidates = set()

        for key_center in key_centers.keys():

            chord_scale, chord_names = build_chord_scale(
                key_centers[key_center], qualities)

            if input_progression[0] in chord_names:
                pre_candidates.add(key_center)

            if len(input_progression) == 1:
                candidates = pre_candidates
                continue

            if len(input_progression) > 1:

                for chord in input_progression[1:]:

                    if chord in chord_names:
                        post_candidates.add(key_center)

                    # else:
                        # pass

                    candidates = set()

                    for i in pre_candidates:
                        if i in post_candidates:
                            candidates.add(i)

            print()

        os.system("clear")

        print()
        print(f"Input progression: {input_progression}")
        print()

        return candidates

    except Exception as e:
        print(f"Oops! Unexpected error: {e}.")
        return ""
