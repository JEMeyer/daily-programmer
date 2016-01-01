import sys, math, re, random

doNotEncode = '[0-9.,:;!?()\s]'

def decoder(path):
    '''
    Input:
        path: filePath - where the key and encoded message exist
    Returns: decoded message
    '''
    # Open file, read in decoding line and encoded input
    with open(path, 'r') as f:
        d = f.readline().split()
        codeCrack = dict(zip(d[1::2], d[0::2]))
        secret = f.readline()

    # Decoded message
    message = ''
    
    # Find the key that matches the beginning of the string, get the value
    # (decoded character) and add it to our ouput. Remove the encoded string
    # from our encoded message
    while len(secret) > 0:
        char = secret[0]
        if re.match(doNotEncode, char):
            message += char
            secret = secret[1:]
        else:
            for key, value in codeCrack.items():
                if secret.startswith(key):
                    message += value
                    secret = secret[len(key):]
            
    # Write decoded message
    with open("decoded.txt", 'w') as f:
        f.write(message)
    
def encoder(path):
    '''
    Input:
        path: File path - raw message
    Returns: Key to decode as well as encoded message
    '''
    # Raw message
    with open(path, 'r') as f:
        rMessage = f.readline()
    
    # Will use log base 2 to find total number of characters per encoding.
    # Will treat g and G as 0 and 1 in binary
    neededKeyChars = math.ceil(math.log(len(''.join(set(re.sub(doNotEncode, '', rMessage)))), 2))
    
    # Encoded message and key
    encoded = ''
    key = {}
    
    # For every character in the raw message, if it is a number or punctuation
    # simply add that to encoded message. Otherwise, if it is not in the
    # dict, add it. If it IS in the dict, add the encoded value to encoded msg
    for char in rMessage:
        if re.match(doNotEncode, char):
            encoded += char
        elif char not in key:
            value = ''.join(random.choice(['g','G']) for _ in range(neededKeyChars))
            while value in key.values():
                value = ''.join(random.choice(['g','G']) for _ in range(neededKeyChars))
            key[char] = value
            encoded += value
        else:
            encoded += key[char]
    
    # Assemble output to make it pretty
    output = ''
    for a, b in key.items():
        output += a + ' ' + b + ' '
    output += '\n' + encoded
    
    # Write encoded message
    with open("encoded.txt", 'w') as f:
        f.write(output)
  
action = sys.argv[1]
input = sys.argv[2]

# Functions take file path
if action == '-decode':
    decoder(input)
elif action == '-encode':
    encoder(input)