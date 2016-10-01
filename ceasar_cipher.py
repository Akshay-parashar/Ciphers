MAX_KEY_SIZE = 26

def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = raw_input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
    print('Enter your message:')
    return raw_input().lower()

def getKey():
    key = 0
    while True:
        print ('Enter the key number (1-%d)' % (MAX_KEY_SIZE))
        key = int(raw_input())
        if (key >=1 and key <= MAX_KEY_SIZE):
            return key

def getTransMessage(mode,key,message):
    if mode == 'd':
        key = -key
    trans = ''

    for char in message:
        if char.isalpha():
            num = ord(char)
            num = (((num - 97)+key)%26)+97
            trans += chr(num)
        else:
            trans += char
    return trans

mode = getMode()
message = getMessage()
key = getKey()

print('Your translated text is: ')
print(getTransMessage(mode,key,message))
            
            
