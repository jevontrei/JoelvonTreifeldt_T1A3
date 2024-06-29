from .chord_builder import build_triad

# This function ...

def build_chord_scale(scale, qualities):
    """_summary_

    Args:
        scale (list): _description_
        qualities (list): _description_

    Returns:
        _type_: _description_
    """
    
    try:
        # Initialise dictionary for storing chords and list for names:
        chord_scale = {}
        names = []
        
        print()
        print(f"In the key of {scale[0][:]} major,")
        
        
        
        for degree in range(7):
            degree += 1
            name, chord = build_triad(
                scale, degree, qualities)
            
            chord_scale[name] = chord
            names.append(name)
            print(f"Chord {degree} is {name}: {chord_scale[name]}")

        return chord_scale, names

    except Exception as e:
        print(f"Oops! Unexpected error: {e}.")
        return ""

