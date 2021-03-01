"""This function decodes a binary string""" 

def decode(s):
    
    decoded_string = "" 

    """Looping through each character"""

    ptr = 0
    while(ptr < len(s)):
        ascii_value = int(s[ptr:ptr+7],2)
        decoded_string = decoded_string + str(chr(ascii_value))
        ptr = ptr + 7

    """Displaying the process of decoding""" 

    print("***** Decoding Process ******")
    print("Binary string to decode : " + s)
    print("decoded string : " + decoded_string)
    print("*****************************\n")

    """Returning the decoded string"""

    return decoded_string



# This call below should decode to 'Hello guys' , Uncomment to test
# decode("1001000110010111011001101100110111101000001100111111010111110011110011")

        





        
        

        
    