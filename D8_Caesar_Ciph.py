alphabet = [
    ' ','a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z',
]

# function for encryption

def encrypt(sentence, key):
    print("Encypting... ")
        
    encrypted = ""
    
    for ch in sentence:
        shifted= alphabet.index(ch) + key 
        mode = shifted % 27     # if it goes out of range (26) it will start from beginning  again
        encrypted += alphabet[mode]
    
    print(f"You encrypted message: {encrypted}")
        
def decrypt(cipher, key):  # function to decrypt
    print("Decrypting... ")
    decrypted = ""
    
    for c in cipher:
        shifted = alphabet.index(c) - key
        mode = shifted % 27
        decrypted += alphabet[mode]

    print(f"You encrypted message: {decrypted}")
    
        
        
end = False

while end != True:
    
    sent = input("Enter Your Sentence to Encrypt: ")
    k = int(input("Enter Your Key(integer): "))

    encrypt(sentence=sent, key=k)

    ci = input("Enter Your Cipher to Decrpyt: ")
    k_1 = int(input("Enter Your Decrption Key(integer): "))

    decrypt(ci,k_1)
    
    choice = input("Enter 'n' to End Program: ").lower()
    if choice == "n":
        end = True


