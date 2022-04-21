
def encrypt(InputString):
    
    lookup = {}
    lookup = {'a':'😀','b':'😃','c':'😄','d':'😁','e':'😅','f':'😂', 'g':'🤣', 'h':'🥲', 'i':'☺️', 'j': '😊', 'k':'😇', 'l':'🙂', 'm':'🙃', 'n':'😉', 'o': '😌'}
    words = InputString.split()
    encryptedString = ''
    for i in words:
        for letter in i:
            if letter in lookup:
                letter = lookup.get(letter)
            encryptedString += letter    
    #print(encryptedString)
    return encryptedString
    
def decrypt(InputCipher, lookup):
    decrypted = ''
    letter = ''
    for val in InputCipher:
        if val in lookup.values():
            keys = [k for k, v in lookup.items() if v == val]
            print(keys[0])
            letter = keys[0]
        else:
            letter = val
        decrypted += letter
    #print(decrypted)
    alphabets = dict.fromkeys(string.ascii_lowercase, 0)
    print(alphabets)
    return decrypted
    
encryptedstr = encrypt('hello i name not Earl')
print(encryptedstr)
lookup = {'a':'😀','b':'😃','c':'😄','d':'😁','e':'😅','f':'😂', 'g':'🤣', 'h':'🥲', 'i':'☺️', 'j': '😊', 'k':'😇', 'l':'🙂', 'm':'🙃', 'n':'😉', 'o': '😌'}
decryptedstr = decrypt(encryptedstr, lookup)
print(decryptedstr)