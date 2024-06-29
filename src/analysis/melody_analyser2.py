# This function ...

def analyse_melody2(mel, keys):
    """_summary_

    Args:
        mel (set): _description_
        keys (dict): _description_

    Returns:
        _type_: _description_
    """

    # THIS FN IS BROKEN! e.g. enter "e,f,gb,g" and it gives a wrong answer

    # try:

    # print()
    # print(f"mel: {mel}, {type(mel)}")
    # print(f"keys: {keys}, {type(keys)}")
    print()

    # Initialise ...
    analysis = []
    checklist = []

    print("-------------------------------------------")

    # Make set subscriptable?:
    mel = list(mel)

    print(f"mel[0]: {mel[0]}")

    for scale in keys:

        if mel[0] in keys[scale]:
            print(f"scale: {scale}")
            analysis.append(scale)
            print(f"analysis: {analysis}")

        for note in mel[1:]:
            print(f"note: {note}")
            print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            if note in keys[scale] and note in analysis:
                print(f"scale: {scale}")
                checklist.append(scale)
                print(f"checklist: {checklist}")

                print("````````````````````````")

            print("////////////////////////")

    print("--------")

    # confidence = {}

    # for key in analysis:
    #     print(f"key: {key}")
    #     occurrence = analysis.count(key)
    #     print(f"occurrence: {occurrence}")
    #     confidence[key] = round(occurrence / len(analysis), 2)
    #     print(f"confidence[key]: {confidence[key]}")
    #     print("--------")

    # print("--------")

    # max_conf = 0

    # likely_keys = []

    # for key in confidence:
    #     print(f"key: {key}")
    #     if confidence[key] > max_conf:
    #         max_conf = confidence[key]
    #         print(f"max_conf: {max_conf}")
    #         likely_keys = [key]
    #         print(f"likely_keys: {likely_keys}")

    #     elif confidence[key] == max_conf:
    #         likely_keys.append(key)
    #         print(f"likely_keys: {likely_keys}")

    #     print("--------")

    return checklist

    # except Exception as e:
    #     print(f"__analyse_melody__ Oops! Unexpected error: {e}.")
    #     return ""


# This function ...


def process_likelihood2(likely_keys):
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
                return f">>> Oof, that's a spicy (or vague) melody! This result won't be very useful! But no shade thrown...\nHere are some potentially compatible major keys anyway: {likely_keys}, each with likelihood {likelihood}."

            else:
                return f">>> Compatible key/s: {likely_keys}, (each) with likelihood {likelihood}."

        else:
            return "Sorry! Please enter valid note names."

    except Exception as e:
        print(f"__process_likelihood__ Oops! Unexpected error: {e}.")
        return ""
