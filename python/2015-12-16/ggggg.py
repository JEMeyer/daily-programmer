import sys, math

def decoder(path):
    '''
    Input:
        path: filePath - where the key and encoded message exist
    Returns: decoded message
    '''
    # Open file, read in decoding line and encoded input
    fo = open(path, 'r')
    d = fo.readline().split()
    codeCrack = dict(zip(d[1::2], d[0::2]))
    secret = fo.readline()
    fo.close()

    # Decoded message
    message = ''
    
    while len(secret) > 0:
        for key, value in codeCrack.items():
            if secret.startswith(key):
                message += value
                secret = secret[len(key):]
        char = secret[0].lower()
        if char != 'g':
            message += char
            secret = secret[1:]
    return message
    
def encoder(rMessage):
    '''
    Input:
        rMessage: String - raw message
    Returns: Key to decode as well as encoded message
    '''
    # Will use log base 2 to find total number of characters per encoding.
    # Will treat g and G as 0 and 1 in binary
    neededKeyChars = math.log(len(rMessage), 2)
    
    # Encoded message and key
    key, 
  
action = sys.argv[1]
input = sys.argv[2]

if action == '-decode':
    print(decoder(input))
elif action == '-encode':
    print(encoder(input))