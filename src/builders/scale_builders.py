# The scale_builder (function?) takes a root note as input and constructs a major scale on that note

def build_all_scales(letters, intervals):
    """_summary_
    """
    # try:
    scales = []
    for i in range(12):
        key = []
        for k in intervals:
            key.append(letters[(i + k) % 12])
        scales.append(key)
    all_scales = dict(zip(letters, scales))
    
    return all_scales
