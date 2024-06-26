def key_analysis(mel, keys):
    """_summary_

    Args:
        mel (_type_): _description_
    """
    print()
    analysis = []
    for note in mel:
        # print(f"Melody note: {note}")
        for scale in keys:
            # print(f"Scale: {scale}")
            # print(f"Scale: {keys[scale]}")
            if note in keys[scale]:
                analysis.append(scale)
                # print(f"Key analysis: {analysis}")
                # print("---------------------------")
            # else:
            #     print("Sorry, note not found.")
            #     print("---------------------------")
            #     analysis = []
            #     break
            #     print(f"Melody fits within the key of {scale}.")
            #     print("This melody combines multiple scales.")
    # print(f"Analysis: {analysis}")

    confidence = {}
    for key in analysis:
        occurrence = analysis.count(key)
        confidence[key] = round(occurrence / len(analysis), 2)
    # print(f"Confidence: {confidence}")

    max_conf = 0
    likely_keys = []
    for key in confidence:
        if confidence[key] > max_conf:
            max_conf = confidence[key]
            likely_keys = [key]
        elif confidence[key] == max_conf:
            likely_keys.append(key)

    # print(max(confidence))

    return likely_keys


def likely_processor(likely_keys):
    """_summary_

    Args:
        likely_keys (_type_): _description_

    Returns:
        _type_: _description_
    """
    if len(likely_keys) > 0:
        likelihood = round(1 / len(likely_keys), 2)
        if likelihood < 0.25:
            return f"Oof, that's a spicy (or vague) melody! This result won't be very useful! But no shade thrown...\nHere are some potentially compatible major keys anyway: {likely_keys}, each with likelihood {likelihood}."
        else:
            # print out a full list of ...
            return f"Most likely key/s: {likely_keys}, (each) with likelihood {likelihood}."
    else:
        return "Error! Please enter valid note names."
