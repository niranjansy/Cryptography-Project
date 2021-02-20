"""This function shall decrypt the binary string"""

def decrypt(binary_string,key):

    decrypted_string = ""

    """replicate the key until it is not less than than binary string"""

    replicated_key = ""
    while(len(replicated_key) < len(binary_string)):
        replicated_key = replicated_key + key
    
    """Printing decryption process"""

    print("****** Printing decryption process *******")
    print("Key : " + key)
    print("Replicated key   : " + replicated_key[:len(binary_string)])
    print("Encrypted String    : " + binary_string)
    
    ptr = 0
    for c in binary_string:
        decrypted_string = decrypted_string + str(int(c)^int(replicated_key[ptr]))
        ptr=ptr+1
    
    print("Decrypted String : " + decrypted_string)
    print("************************************")

    """Returning decrypted string"""

    return decrypted_string

# decrypt("1001000110010111011001101100110111101000001100111111010111110011110011","100101")
    