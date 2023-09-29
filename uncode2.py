import regex as re


def un_code2(message3):

    my_text = message3
    pattern = r"av+"
    nstr = re.sub(pattern, "", my_text)

    output = nstr
    return output
