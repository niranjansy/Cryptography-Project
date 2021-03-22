from colors import bcolors
"""This function shall encrypt the binary string"""

def encrypt(binary_string,key):

    encrypted_string = ""

    """replicate the key until it is not less than than binary string"""

    replicated_key = ""
    while(len(replicated_key) < len(binary_string)):
        replicated_key = replicated_key + key
    
    """Printing encryption process"""

    print("****** Printing encryption process *******")

    print(bcolors.BOLD + bcolors.OKGREEN + "Key : " + bcolors.ENDC + key)
    print(bcolors.BOLD + bcolors.OKGREEN + "Replicated key   : " + bcolors.ENDC + replicated_key[:len(binary_string)])
    print(bcolors.BOLD + bcolors.OKGREEN + "Binary String    : " + bcolors.ENDC + binary_string)
    
    ptr = 0
    for c in binary_string:
        encrypted_string = encrypted_string + str(int(c)^int(replicated_key[ptr]))
        ptr=ptr+1
    
    print(bcolors.BOLD + bcolors.OKGREEN + "Encrypted String : " + bcolors.ENDC + encrypted_string)

    print("************************************\n")
    
    """Returning the encrypted string""" 

    return encrypted_string

# encrypt("1001000110010111011001101100110111101000001100111111010111110011110011","100101")
    