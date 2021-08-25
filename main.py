alphabets="abcdefghijklmnopqrstuvwxyz"
message=input("Enter the message to encrypt: ")
encrypt,decrypt="",""
key=5

for letter in message:
    new_position=(alphabets.find(letter)+key)%len(alphabets)
    encrypt+=alphabets[new_position]

for letter in encrypt:
    new_position=(alphabets.find(letter)-key)%len(alphabets)
    decrypt+=alphabets[new_position]


print("Encrypted message:",encrypt)
print("Decrypted message:",decrypt)
