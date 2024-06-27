def build_triad(scale, degree, qualities):
    """_summary_

    Args:
        scale (list): _description_
        degree (int): _description_
        qualities (list): _description_

    Returns:
        _type_: _description_
    """
    print()
    # print(f"Scale: {scale}, {type(scale)}")
    # print(f"Degree: {degree}, {type(degree)}")
    # print(f"Qualities: {qualities}, {type(qualities)}")
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
