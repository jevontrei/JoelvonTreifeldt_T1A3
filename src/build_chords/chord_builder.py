def build_triad(scale_list, degree_int, qualities_list):
    """_summary_

    Args:
        scale_list (list): _description_
        degree_int (int): _description_
        qualities_list (list): _description_

    Returns:
        _type_: _description_
    """
    try:
        print()
        # print(f"scale_list: {scale_list}, {type(scale_list)}")
        # print(f"degree_int: {degree_int}, {type(degree_int)}")
        # print(f"qualities_list: {qualities_list}, {type(qualities_list)}")
        # Offest zero indexing:
        degree_int -= 1
        triad = []
        # Define ...
        name = scale_list[degree_int] + qualities_list[degree_int]
        for k in range(3):
            # print(f"This index: {(degree_int + (k * 2)) % 7}")
            triad.append(scale_list[(degree_int + (k * 2)) % 7])
            # print(f"Progress shot of triad: {triad}")
        return name, triad
    
    except Exception as e:
        print(f"Oops! Unexpected error: {e}.")
        return ""