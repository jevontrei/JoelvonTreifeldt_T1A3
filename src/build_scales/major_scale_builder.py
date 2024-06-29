# This function takes a root note as input and constructs a major scale on that note (for all 12 root notes)

def build_all_scales(letters, intervals):
    """_summary_

    Args:
        letters (_type_): _description_
        intervals (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    try:
        # Initialise ...
        scales = []
        
        for i in range(12):
            key = []
            for k in intervals:
                key.append(letters[(i + k) % 12])
                
            scales.append(key)
            
        all_scales = dict(zip(letters, scales))
        
        return all_scales
    
    except Exception as e:
        print(f"Oops! Unexpected error: {e}.")
        return ""
