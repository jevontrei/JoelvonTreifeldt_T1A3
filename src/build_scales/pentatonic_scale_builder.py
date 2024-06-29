# This function takes a root note and a quality as input and constructs one pentatonic scale on that note
def build_penta(tonic, root_notes, quality):
    """_summary_

    Args:
        tonic (_type_): _description_
        root_notes (_type_): _description_
        quality (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    try:
        # Define scale intervals:
        major_penta_intervals = [0, 2, 4, 7, 9]
        minor_penta_intervals = [0, 3, 5, 7, 10]

        # Initialise output list:
        penta = []

        print()

        while True:
            if quality == "maj":
                for k in major_penta_intervals:
                    penta.append(
                        root_notes[(root_notes.index(tonic) + k) % 12])
                    
                return penta

            elif quality == "min":
                for k in minor_penta_intervals:
                    penta.append(
                        root_notes[(root_notes.index(tonic) + k) % 12])
                    
                return [penta]

            elif quality == "pls":
                penta = []
                return penta

            else:
                print(
                    "Oops! Please enter a valid root note and 'maj' or 'min' as the quality, or enter 'exit, pls'.")
                
                penta = []
                return penta

    except Exception as e:
        print(f"Oops! Unexpected error: {e}.")
        return ""
