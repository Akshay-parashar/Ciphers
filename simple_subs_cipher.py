ALPHA = 'abcdefghijklmnopqrstuvwxyz'

def enc(mess,key):
    ciph = ''
    mess = filter(str.isalpha,mess.lower())
    key = key.lower()
    for char in mess:
        ch = key[ALPHA.index(char)] #replacing the char in message with char in key
        ciph += ch
    return ciph

def dec(mess,key):
    text = ''
    mess = filter(str.isalpha,mess.lower())
    key = key.lower()
    for char in mess:
        ch = ALPHA[key.index(char)] #doing extacly the opposite of encryption
        text += ch
    return text



