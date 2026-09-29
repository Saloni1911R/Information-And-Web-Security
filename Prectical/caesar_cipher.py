class caesar:
  def __init__(self, normal_text, shift):
    self.s = shift
    self.normal = normal_text

  def caesar_cipher(self):
    result = ''
    
    for ch in self.normal:
      if ch.isupper():
        result += chr((ord(ch) - ord('A') + self.s) % 26 + ord('A'))
      elif ch.islower():
        result += chr((ord(ch) - ord('a') + self.s) % 26 + ord('a'))
      else:
        result += ch

    return result

  def caesar_decipher(self):
    result = ''
    for ch in self.normal:
      if ch.isupper():
        result += chr((ord(ch) - ord('A') - self.s) % 26 + ord('A'))
      elif ch.islower():
        result += chr((ord(ch) - ord('a') - self.s) % 26 + ord('a'))
      else:
        result += ch
    return result

text = input("Enter Plain Text: ")
shift = int(input("Enter Key: "))

cipher_instance = caesar(text, shift)
a = cipher_instance.caesar_cipher()
print(a)

decoder = caesar(a, shift)
b = decoder.caesar_decipher()
print(b) 
