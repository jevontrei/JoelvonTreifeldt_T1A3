# This function ...
def format_output_notes(rename):
    """_summary_

    Args:
        rename (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    ### unnecessary bc i've already cleaned it all up in .input_formatting:?
    try:
        ### except:
        ### catch:
        ### raise:
        for key in range(len(rename)):
            if rename[key][-1] == "_":
                rename[key] = rename[key][0]
                
        return rename

    except Exception as e:
        print(f"__format_output_notes__ Oops! Unexpected error: {e}.")
        return ""


### This function ... DELET?:

def format_output_chords():
    """_summary_

    Returns:
        _type_: _description_
    """
    
    try:
        return

    except Exception as e:
        print(f"__format_output_chords__ Oops! Unexpected error: {e}.")
        return ""
