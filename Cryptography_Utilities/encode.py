from colors import bcolors
"""This function encodes a string to binary""" 

def encode(s):
    
    encoded_binary_string = "" 

    """Looping through each character"""

    for c in s:
        ascii_value = ord(c)
        binary_string = bin(ascii_value)[2:]

        """Prepending 0s to make length 7"""

        while(len(binary_string)<7):
            binary_string = "0" + binary_string
        
        encoded_binary_string = encoded_binary_string + binary_string
        
    """Displaying the process of encoding""" 

    print("***** Encoding Process ******")
    print(bcolors.BOLD + bcolors.OKGREEN + "String to encode : " + bcolors.ENDC + s)
    print(bcolors.BOLD + bcolors.OKGREEN + "Encoded string : "+ bcolors.ENDC + str(encoded_binary_string))
    print("*****************************\n")

    """Returning the encoded string"""

    return encoded_binary_string


# This call below should decode to '1001000110010111011001101100110111101000001100111111010111110011110011' , Uncomment to test
# encode("Hello guys")

        





        
        

        
    