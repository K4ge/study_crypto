# 摩斯密码字典
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}

# 反转摩斯密码字典
REVERSED_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def morse_to_text(morse_code):
    words = morse_code.split('   ')  # 每个词由三个空格分隔
    decoded_message = []
    for word in words:
        letters = word.split(' ')  # 每个字母由一个空格分隔
        decoded_word = ''.join(REVERSED_MORSE_CODE_DICT[letter] for letter in letters)
        decoded_message.append(decoded_word)
    return ' '.join(decoded_message)

# 摩斯密码字符串
morse_code = ".. .-.. --- ...- . -.-- --- ..-"

# 解码
decoded_message = morse_to_text(morse_code)

print(decoded_message)