def analyse_progression(input_progression, key_centers):
    print()
    input_progression = input_progression.split(",")
    # use format chord module instead of this:
    for i in range(len(input_progression)):
        input_progression[i] = input_progression[i].strip(" ")
    print(input_progression)
    candidates = []
    # fix this:
    for chord in input_progression:
        for key_center in key_centers.keys():
            if chord in key_centers[key_center]:
                candidates.append(chord)
    print(candidates)
    print(f"These chords fit within the key/s of .... The Roman Numeral Analysis is ....")
    return "finish me"
