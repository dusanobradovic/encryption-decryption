keys = "abcdefghijklmnopqrstuvwxyzQWERTZUIOPASDFGHJKLYXCVBNM1234567890"
message = input("Enter the message to encrypt: ")
encrypt, decrypt= "",""
num = 5

for letter in message:
    new_position = (keys.find(letter) + num) % len(keys)
    encrypt += keys[new_position]

for letter in encrypt:
    new_position = (keys.find(letter) - num) % len(keys)
    decrypt += keys[new_position]

if __name__ == "__main__":
    
    print("Starting program")
    print("Encrypted message: ", encrypt)
    print("Decrypted message: ", decrypt)
