# This function ...

def analyse_melody(mel, keys):
    """_summary_

    Args:
        mel (set): _description_
        keys (dict): _description_

    Returns:
        _type_: _description_
    """

    try:
        print()

        # Initialise ...
        compatible = []

        for scale in keys:
            if all(n in keys[scale] for n in mel):
                compatible.append(scale)

        return compatible

    # except 
    except Exception as e:
        print(f"__analyse_melody__ >>> Oops! Unexpected error: {e}.")
        return ""
