import regex as re


def code_2(message2):
    my_text = message2
    mapping = re.sub(r"[aeiou]", lambda x: "av" + x.group(0), my_text)

    output = mapping
    return output
