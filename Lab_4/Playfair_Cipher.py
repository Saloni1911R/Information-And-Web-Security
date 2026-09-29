def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    seen = set()
    
    for char in key:
        if char.isalpha() and char not in seen:
            seen.add(char)
            matrix.append(char)
            
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            matrix.append(char)
            
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == char:
                return r, c
    return None

def prepare_text(plaintext):
    text = plaintext.upper().replace("J", "I")
    text = "".join([c for c in text if c.isalpha()])
    
    prepared = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i + 1 < len(text) else 'X'
        
        if a == b:
            prepared.append(a + 'X')
            i += 1
        else:
            prepared.append(a + b)
            i += 2
            
    if len(prepared[-1]) == 1:
        prepared[-1] += 'X'
        
    return prepared

def playfair_encrypt(prepared_pairs, matrix):
    ciphertext = ""
    for a, b in prepared_pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        
        if r1 == r2:  # Same row
            ciphertext += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:  # Same column
            ciphertext += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        else:  # Rectangle rule
            ciphertext += matrix[r1][c2] + matrix[r2][c1]
            
    return ciphertext

def playfair_decrypt(ciphertext, matrix):
    plaintext = ""
    pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    
    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        
        if r1 == r2:  # Same row
            plaintext += matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:  # Same column
            plaintext += matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
        else:  # Rectangle rule
            plaintext += matrix[r1][c2] + matrix[r2][c1]
            
    return plaintext

# Execution
key = "MONARCHY"
matrix = generate_matrix(key)

# Part A: Encryption
plaintext = "HELLO"
pairs = prepare_text(plaintext)
encrypted = playfair_encrypt(pairs, matrix)

print(f"Keyword     : {key}")
print(f"Plain Text  : {plaintext}")
print(f"Pairs       : {' '.join(pairs)}")
print(f"Cipher Text : {encrypted}\n")

# Part B: Decryption
decrypted = playfair_decrypt(encrypted, matrix)
print(f"Cipher Text : {encrypted}")
print(f"Decrypted   : {decrypted}")
