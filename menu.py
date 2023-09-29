from decoding_text import de_coding
from text_coding import coding


while True:
    dla = input(f"What do you what to do? A) text coding, B) decoding a text or C) to quit [A/B/C]? : ").lower()
    if dla == "a":
        message = input("Type your text here: ").lower()
        result = coding(message)
        print(result)
    elif dla == "b":
        message1 = input("Type your coding message here: ").lower()
        result = de_coding(message1)
        print(result)
    elif dla == "c":
        break
    else:
        print("I don't understand that!")