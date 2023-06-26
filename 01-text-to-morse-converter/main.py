

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
  }

TEXT_CODE_DICT = {v: k for (k, v) in MORSE_CODE_DICT.items()}

def to_morse(message):
    result = []
    for char in message:
        if char == ' ':
            result.append(' ')
        else:
            result.append(MORSE_CODE_DICT[char.upper()])
    return result


def to_text(message):
    result = []
    for code in message:
        if code == ' ':
            result.append(' ')
        else:
            result.append(TEXT_CODE_DICT[code])
    return result


textInput = input("Input your text: ")
morse = to_morse(textInput)
print(f"morse: {morse}")
original = to_text(morse)
print(f"original: {original}")
