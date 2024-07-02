ceaser = \
r'''
shift = 3
ciphertext = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext
'''

ceaserDecryptor = \
r'''
shift = 3
decrypted_text = ""

for char in flag:
    if char.isalpha():
        shifted = chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text
'''

atbash = \
r'''
ciphertext = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  
        ciphertext += reversed_char
    else:
        ciphertext += char

flag = ciphertext
'''

atbashDecryptor = \
r'''
decrypted_text = ""

for char in flag:
    if char.isalpha():
        reversed_char = chr(155 - ord(char.upper()))  # 155 = 65 (A) + 90 (Z)
        decrypted_text += reversed_char
    else:
        decrypted_text += char

flag = decrypted_text
'''

vignere = \
"""
key = "KEY"
ciphertext = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext
"""

vignereDecryptor = \
r'''
key = "KEY"
decrypted_text = ""
key_length = len(key)

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = key[i % key_length].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
    else:
        decrypted_text += char

flag = decrypted_text
'''

playfair = \
"""
key = "KEYWORD"
key_matrix = []
used = []


for char in key.upper():
    if char not in used and char != 'J':
        key_matrix.append(char)
        used.append(char)

for i in range(65, 91):
    char = chr(i)
    if char not in used and char != 'J':
        key_matrix.append(char)
        used.append(char)

key_matrix = [key_matrix[i * 5:(i + 1) * 5] for i in range(5)]

def find_position(char):
    for row in range(5):
        for col in range(5):
            if key_matrix[row][col] == char:
                return row, col


flag = flag.replace('J', 'I')
if len(flag) % 2 != 0:
    flag += 'X'

ciphertext = ""
i = 0
while i < len(flag):
    a = flag[i]
    b = flag[i + 1]
    row1, col1 = find_position(a)
    row2, col2 = find_position(b)
    if row1 == row2:    
        ciphertext += key_matrix[row1][(col1 + 1) % 5]
        ciphertext += key_matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        ciphertext += key_matrix[(row1 + 1) % 5][col1]
        ciphertext += key_matrix[(row2 + 1) % 5][col2]
    else:
        ciphertext += key_matrix[row1][col2]
        ciphertext += key_matrix[row2][col1]
    i += 2

flag = ciphertext
"""

playfairDecryptor = \
r'''
key = "KEYWORD"
key_matrix = []
used = []

# Generate key matrix
for char in key.upper():
    if char not in used and char != 'J':
        key_matrix.append(char)
        used.append(char)

for i in range(65, 91):
    char = chr(i)
    if char not in used and char != 'J':
        key_matrix.append(char)
        used.append(char)

key_matrix = [key_matrix[i * 5:(i + 1) * 5] for i in range(5)]

def find_position(char):
    for row in range(5):
        for col in range(5):
            if key_matrix[row][col] == char:
                return row, col
    return None

decrypted_text = ""
i = 0
while i < len(flag):
    a = flag[i]
    b = flag[i + 1] if i + 1 < len(flag) else 'X'
    row1, col1 = find_position(a)
    row2, col2 = find_position(b)
    
    if row1 is None or row2 is None:
        print("Error: Character not found in key matrix.")
        break
    
    if row1 == row2:
        decrypted_text += key_matrix[row1][(col1 - 1) % 5]
        decrypted_text += key_matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        decrypted_text += key_matrix[(row1 - 1) % 5][col1]
        decrypted_text += key_matrix[(row2 - 1) % 5][col2]
    else:
        decrypted_text += key_matrix[row1][col2]
        decrypted_text += key_matrix[row2][col1]
    i += 2

flag = decrypted_text
'''

hill = \
"""
key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])  
flag = flag.upper().replace(' ', '')
if len(flag) % 3 != 0:
    flag += 'X' * (3 - len(flag) % 3)

def text_to_numbers(text):
    return [ord(char) - 65 for char in text]

def numbers_to_text(numbers):
    return ''.join(chr(num + 65) for num in numbers)

plaintext_numbers = text_to_numbers(flag)
ciphertext_numbers = []

for i in range(0, len(plaintext_numbers), 3):
    block = np.array(plaintext_numbers[i:i + 3])
    encrypted_block = np.dot(key_matrix, block) % 26
    ciphertext_numbers.extend(encrypted_block)

ciphertext = numbers_to_text(ciphertext_numbers)
flag = ciphertext
"""

hillDecryptor = \
r'''
key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])  # 3x3 key matrix
inverse_key_matrix = np.linalg.inv(key_matrix).astype(int) % 26  # Find the modular inverse of the key matrix

def text_to_numbers(text):
    return [ord(char) - 65 for char in text]

def numbers_to_text(numbers):
    return ''.join(chr(num + 65) for num in numbers)

ciphertext_numbers = text_to_numbers(flag)
decrypted_text_numbers = []

for i in range(0, len(ciphertext_numbers), 3):
    block = np.array(ciphertext_numbers[i:i + 3])
    decrypted_block = np.dot(inverse_key_matrix, block) % 26
    decrypted_text_numbers.extend(decrypted_block)

decrypted_text = numbers_to_text(decrypted_text_numbers)
flag = decrypted_text
'''

substitution = \
"""
key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  
ciphertext = ""

for char in flag:
    if char.isalpha():
        index = ord(char.upper()) - 65
        ciphertext += key[index]
    else:
        ciphertext += char

flag = ciphertext
"""

substitutionDecryptor = \
r'''
key = "QWERTYUIOPLKJHGFDSAZXCVBNM"  # Substitution key
decrypted_text = ""
inverse_key = {key[i]: chr(65 + i) for i in range(26)}

for char in flag:
    if char.isalpha():
        decrypted_text += inverse_key[char.upper()]
    else:
        decrypted_text += char

flag = decrypted_text
'''

transposition = \
"""
key = 3  
ciphertext = [''] * key

for col in range(key):
    pointer = col
    while pointer < len(flag):
        ciphertext[col] += flag[pointer]
        pointer += key

flag = ''.join(ciphertext)
"""

transpositionDecryptor = \
r'''
key = 3  # Number of columns
num_cols = key
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

decrypted_text = [''] * num_rows
col = 0
row = 0

for char in flag:
    decrypted_text[row] += char
    row += 1
    if row == num_rows:
        row = 0
        col += 1

flag = ''.join(decrypted_text)
'''

railfence = \
"""
key = 3  
ciphertext = [''] * key
rail = 0
direction = 1

for char in flag:
    ciphertext[rail] += char
    rail += direction
    if rail == 0 or rail == key - 1:
        direction = -direction

flag = ''.join(ciphertext)
"""

railfenceDecryptor = \
r'''
key = 3  # Number of rails
rail_pattern = [['\n'] * len(flag) for _ in range(key)]
direction_down = False
row, col = 0, 0

for char in flag:
    if row == 0 or row == key - 1:
        direction_down = not direction_down
    rail_pattern[row][col] = '*'
    col += 1
    row += 1 if direction_down else -1

index = 0
for i in range(key):
    for j in range(len(flag)):
        if rail_pattern[i][j] == '*' and index < len(flag):
            rail_pattern[i][j] = flag[index]
            index += 1

decrypted_text = []
row, col = 0, 0
for i in range(len(flag)):
    if row == 0 or row == key - 1:
        direction_down = not direction_down
    if rail_pattern[row][col] != '*':
        decrypted_text.append(rail_pattern[row][col])
        col += 1
    row += 1 if direction_down else -1

flag = ''.join(decrypted_text)
'''

columnarTransposition = \
"""
key = "3214"  
num_cols = len(key)
num_rows = len(flag) // num_cols + (len(flag) % num_cols != 0)
grid = [[''] * num_cols for _ in range(num_rows)]

for i, char in enumerate(flag):
    row = i // num_cols
    col = i % num_cols
    grid[row][int(key[col]) - 1] = char

ciphertext = ''.join(sum(grid, []))
flag = ciphertext
"""

columnarTranspositionDecryptor = \
r'''
key = "3214"  # Column order
num_cols = len(key)
num_rows = len(flag) // num_cols
if len(flag) % num_cols:
    num_rows += 1

grid = [[''] * num_cols for _ in range(num_rows)]
col_lengths = [0] * num_cols
sorted_key = sorted((char, i) for i, char in enumerate(key))

index = 0
for char, col in sorted_key:
    for row in range(num_rows):
        if index < len(flag):
            grid[row][col] = flag[index]
            index += 1

decrypted_text = ''.join(grid[row][col] for row in range(num_rows) for col in range(num_cols))

flag = decrypted_text
'''

autokey = \
"""
key = "KEY"
ciphertext = ""
extended_key = key + flag

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 + ord(key_char) - 65) % 26) + 65)
        ciphertext += shifted
    else:
        ciphertext += char

flag = ciphertext
"""
autokeyDecryptor = \
r'''
key = "KEY"
decrypted_text = ""
extended_key = key

for i, char in enumerate(flag):
    if char.isalpha():
        key_char = extended_key[i].upper()
        shifted = chr(((ord(char.upper()) - 65 - (ord(key_char) - 65)) % 26) + 65)
        decrypted_text += shifted
        extended_key += shifted
    else:
        decrypted_text += char

flag = decrypted_text
'''

cipherTemplates = [
    ceaser,
    atbash,
    vignere,
    playfair,
    hill,
    substitution,
    transposition,
    columnarTransposition,
    autokey
]

cipherCodes = {
    "ceaser": [ceaser, ceaserDecryptor],
    "atbash": [atbash, atbashDecryptor],
    "vignere": [vignere, vignereDecryptor],
    # "playfair": [playfair, playfairDecryptor],
    # "hill": [hill, hillDecryptor],
    "substitution": [substitution, substitutionDecryptor],
    "transposition": [transposition, transpositionDecryptor],
    # "columnarTransposition": [columnarTransposition, columnarTranspositionDecryptor],
    "autokey": [autokey, autokeyDecryptor],
}