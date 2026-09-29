class monoalphabetic:
    def __init__(self, key):
        self.key = key.upper()
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.encrypt_table=str.maketrans(self.alphabet, self.key)

    def encrypt(self, plaintext):
        return plaintext.upper().translate(self.encrypt_table)

    def decreypt(self, ciphertext):
        decrypt_table = str.maketrans(self.key, self.alphabet)
        return ciphertext.upper().translate(decrypt_table)
        

key = "QWERTYUIOPASDFGHJKLZXCVBNM"
plain = input("Enter Plain Text: ").upper()

cipher = monoalphabetic(key)
encrypted_text = cipher.encrypt(plain)
print(encrypted_text)

decrypted_text = cipher.decreypt(encrypted_text)
print(decrypted_text)