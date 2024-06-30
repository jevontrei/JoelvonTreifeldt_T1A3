# This function ...

def build_triad(scale, degree, qualities):
    """_summary_

    Args:
        scale (list): _description_
        degree (int): _description_
        qualities (list): _description_

    Returns:
        _type_: _description_
    """
    try:
        print()
        # Offest zero indexing:
        degree -= 1
        
        # Initialise ...
        triad = []
        
        # Define ...
        name = scale[degree] + qualities[degree]
        
        for k in range(3):
            triad.append(scale[(degree + (k * 2)) % 7])
            
        return name, triad
    
    except Exception as e:
        print(f"__build_triad__ >>> Oops! Unexpected error: {e}.")
        return ""