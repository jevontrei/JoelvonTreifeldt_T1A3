
# i'm repeating myself twice here ... make it more elegant and just do it all in one
def format_input(notes):
    # try:
    # except:
    # catch:
    # raise:
    # print(notes)
    if type(notes) == str:
        notes = notes.strip(" ").upper()
        if len(notes) == 2:
            notes = notes[0] + notes[1].lower()
            input = notes
        elif len(notes) == 1:
            input = notes + "_"
        # print(f"Input: {input}")
        else:
            input = f"Error when parsing '{notes}'! Please enter note name with 1 or 2 characters."
            return
    elif type(notes) == list:
        for i in range(len(notes)):
            notes[i] = notes[i].upper().strip(" ")
            # print(f"mel[i]: {mel[i]}")
            if len(notes[i]) == 2:
                notes[i] = notes[i][0] + notes[i][1].lower()
                # print(melody[i])
                input = notes
            elif len(notes[i]) == 1:
                notes[i] += "_"
                # print(melody[i])
                input = notes
            else:
                input = f"Error when parsing '{notes[i]}'! Please enter note name/s with 1 or 2 characters."
                break
    else:
        # TypeError or ValueError?
        print("TypeError! Please enter a string or a list.")
        return
    return input


def format_input_chords():
    # try:
    # except:
    # catch:
    # raise:
    return
