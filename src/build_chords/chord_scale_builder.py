from .chord_builder import build_triad


def build_chord_scale(scale_list, qualities_list):
    """_summary_

    Args:
        scale_list (list): _description_
        qualities_list (list): _description_

    Returns:
        _type_: _description_
    """
    try:

        # print(f"scale_list: {scale_list}, {type(scale_list)}")
        # print(f"qualities_list: {qualities_list}, {type(qualities_list)}")

        # Initialise dictionary for storing chords:
        chord_scale = {}
        print()
        print(f"In the key of {scale_list[0][:]} major, the chord scale is:")
        names = []
        for degree in range(7):
            degree += 1
            name, chord = build_triad(
                scale_list, degree, qualities_list)
            chord_scale[name] = chord
            names.append(name)
            print(f"Chord {degree} is {name}: {chord_scale[name]}")

            # append to list and return?

        return chord_scale, names

    except Exception as e:
        print(f"Oops! Unexpected error: {e}.")
        return ""

# def build_all_chord_scales():
