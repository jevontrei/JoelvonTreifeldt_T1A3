from .chord_builder import build_triad


def build_chord_scale(scale, qualities):
    """_summary_

    Args:
        scale (_type_): _description_
        qualities (_type_): _description_
    """
    # print(f"Scale: {scale}, {type(scale)}")
    # print(f"Degree: {scale}, {type(scale[0])}")
    # print(f"Qualities: {qualities}, {type(qualities)}")

    # Initialise dictionary for storing chords:
    chord_scale = {}
    print()
    print(f"In the key of {scale[0][:]},")
    for degree in range(7):
        degree += 1
        name, chord = build_triad(
            scale, degree, qualities)
        chord_scale[name] = chord
        # print(chord_scale)
        print(f"Chord {degree} is {name}: {chord_scale[name]}")

        # append to list and return?

    return chord_scale
