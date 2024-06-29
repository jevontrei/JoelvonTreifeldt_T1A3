# This function ...

def analyse_melody(mel, keys):
    """_summary_

    Args:
        mel (_type_): _description_
        keys (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    try:
        print()
        
        analysis = []
        
        for note in mel:
            for scale in keys:
                if note in keys[scale]:
                    analysis.append(scale)

        confidence = {}
        
        for key in analysis:
            occurrence = analysis.count(key)
            confidence[key] = round(occurrence / len(analysis), 2)

        max_conf = 0
        
        likely_keys = []
        
        for key in confidence:
            if confidence[key] > max_conf:
                max_conf = confidence[key]
                likely_keys = [key]
                
            elif confidence[key] == max_conf:
                likely_keys.append(key)

        return likely_keys

    except Exception as e:
        print(f"Oops! Unexpected error: {e}.")
        return ""


# This function ...


def process_likelihood(likely_keys):
    """_summary_

    Args:
        likely_keys (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    try:
        if len(likely_keys) > 0:
            likelihood = round(1 / len(likely_keys), 2)
            if likelihood < 0.25:
                return f"Oof, that's a spicy (or vague) melody! This result won't be very useful! But no shade thrown...\nHere are some potentially compatible major keys anyway: {likely_keys}, each with likelihood {likelihood}."
            
            else:
                return f"Most likely key/s: {likely_keys}, (each) with likelihood {likelihood}."
            
        else:
            return "Error! Please enter valid note names."

    except Exception as e:
        print(f"Oops! Unexpected error: {e}.")
        return ""
