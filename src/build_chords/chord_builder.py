def build_triad(scale, degree, qualities):
    # print(f"Scale: {scale}, Degree: {degree}")
    # Offest zero indexing:
    degree -= 1
    triad = []
    # Define ...
    name = scale[degree] + qualities[degree]
    for k in range(3):
        # print(f"This index: {(degree + (k * 2)) % 7}")
        triad.append(scale[(degree + (k * 2)) % 7])
        # print(f"Progress shot of triad: {triad}")
    return name, triad
