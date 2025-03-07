def generate_playfair_matrix(key):
    key = key.upper().replace("J", "I")  # Treat I and J as the same
    key = "".join(dict.fromkeys(key))  # Remove duplicates
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = list(key)
    
    for letter in alphabet:
        if letter not in matrix:
            matrix.append(letter)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join([char for char in text if char.isalpha() or char.isspace()])
    prepared_text = ""
    i = 0
    
    while i < len(text):
        a = text[i]
        if a == ' ':
            prepared_text += ' '
            i += 1
            continue
        b = text[i+1] if i+1 < len(text) and text[i+1] != ' ' else 'X'
        
        if a == b:
            prepared_text += a + 'X'
            i += 1
        else:
            prepared_text += a + b
            i += 2
    
    if len(prepared_text.replace(" ", "")) % 2 != 0:
        prepared_text += 'X'
    
    return prepared_text

def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = prepare_text(plaintext)
    ciphertext = ""
    
    i = 0
    while i < len(plaintext):
        if plaintext[i] == ' ':
            ciphertext += ' '
            i += 1
            continue
        a, b = plaintext[i], plaintext[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        
        if row1 == row2:  # Same row
            ciphertext += matrix[row1][(col1+1) % 5] + matrix[row2][(col2+1) % 5]
        elif col1 == col2:  # Same column
            ciphertext += matrix[(row1+1) % 5][col1] + matrix[(row2+1) % 5][col2]
        else:  # Rectangle rule
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
        
        i += 2
    
    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = ""
    
    i = 0
    while i < len(ciphertext):
        if ciphertext[i] == ' ':
            plaintext += ' '
            i += 1
            continue
        a, b = ciphertext[i], ciphertext[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        
        if row1 == row2:  # Same row
            plaintext += matrix[row1][(col1-1) % 5] + matrix[row2][(col2-1) % 5]
        elif col1 == col2:  # Same column
            plaintext += matrix[(row1-1) % 5][col1] + matrix[(row2-1) % 5][col2]
        else:  # Rectangle rule
            plaintext += matrix[row1][col2] + matrix[row2][col1]
        
        i += 2
    
    return plaintext

# User Input
key = input("Enter the encryption key: ").strip()
plaintext = input("Enter the plaintext message: ").strip()
ciphertext = playfair_encrypt(plaintext, key)
decrypted_text = playfair_decrypt(ciphertext, key)

print(f"Key: {key}")
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
