def coding(message):
    text = message
    letters_mapping = dict(a="t", b="u", c="v", d="w", e="x", f="y", g="z", h="a", i="b", j="c", k="d", l="e", m="f",
                           n="g", o="h", p="i", q="j", r="k", s="l", t="m", u="n", v="o", w="p", x="q", y="r", z="s",
                           A="t", B="u", C="v", D="w", E="x", F="y", G="z", H="a", I="b", J="c", K="d", L="e", M="f",
                           N="g", O="h", P="i", Q="j", R="k", S="l", T="m", U="n", V="o", W="p", X="q", Y="r", Z="s"
                           )
    letters2_mapping = {
        " ": " ",
        "é": "(",
        "É": "(",
        "è": ")",
        "È": ")",
        "ê": "¤",
        "Ê": "¤",
        "@": "¾",
        "#": "<",
        "=": ">",
        "!": ";",
        ":": "±",
        ";": "²",
        "?": "+",
        "$": "/",
        ",": "?",
        "'": "¦",
        ".": "-",
        "+": "|",
        "-": "½",
        "*": "¼",
        "/": "$",
        "1": "^",
        "2": "[",
        "3": "]",
        "4": "{",
        "5": "}",
        "6": "¶",
        "7": "§",
        "8": "~",
        "9": "£",
        "0": "¢",
        "\n": "\n"
    }
    output = ""
    for ch in text:
        output += letters_mapping.get(ch, "") + "" + letters2_mapping.get(ch, "") + ""
    return output
