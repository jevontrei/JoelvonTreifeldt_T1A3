# This function ...
def format_output(rename):
    """_summary_

    Args:
        most_likely_key (_type_): _description_

    Returns:
        _type_: _description_
    """
    # try:  # unnecessary bc i've already cleaned it all up in .input_formatting?
    # except:
    # catch:
    # raise:
    for key in range(len(rename)):
        if rename[key][-1] == "_":
            rename[key] = rename[key][0]
    return rename

# This function ...

def format_output_chords():
    # try:
    # except:
    # catch:
    # raise:
    return
