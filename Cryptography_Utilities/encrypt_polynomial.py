from Cryptography_Utilities.encrypt import encrypt
from Cryptography_Utilities.encode import encode
# Uncomment the below 2 lines and comment the above 2 lines for running test_polynomial.py
# from encrypt import encrypt   
# from encode import encode

def encrypt_polynomial(polynomial, key):
    """
    This function accepts a list of polynomial coefficients
    and returns an encrypted string.
    """
    string = ""
    for coeff in polynomial:
        string += str(coeff)
        string += " "
    encoded_string = encode(string)
    encoded_key = str(bin(key)[2:])
    encrypted_string = encrypt(encoded_string, encoded_key)
    return encrypted_string 


    

