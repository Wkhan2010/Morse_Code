MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}


def text_to_morse(text):
    morse_code = ''
    for char in text:
        if char.upper() in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char.upper()] + ' '
        else:
            morse_code += char
    return morse_code.strip()


def morse_to_text(morse_code):
    text = ''
    morse_code = morse_code.split(' ')
    for code in morse_code:
        for key, value in MORSE_CODE_DICT.items():
            if value == code:
                text += key
                break
        else:
            text += code
    return text


# Example usage
input_text = 'HELLO WORLD'
morse_code = text_to_morse(input_text)
print(f'Morse code for "{input_text}": {morse_code}')

input_morse = '- .... . / .-- --- .-. .-.. -..'
text = morse_to_text(input_morse)
print(f'Text for "{input_morse}": {text}')
