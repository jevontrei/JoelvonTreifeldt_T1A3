def triad_builder(scale, degree):
    print(f"Scale: {scale}, Degree: {degree}")
    # Offest zero indexing:
    degree -= 1
    triad = []
    for k in range(3):
        # print(f"This index: {(degree + (k * 2)) % 7}")
        triad.append(scale[(degree + (k * 2)) % 7])
        # print(f"Progress shot of triad: {triad}")
    return triad


def chord_scale_builder(scale):
    return

# def seventh_chord_builder():
#     return
