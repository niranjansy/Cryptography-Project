from Cryptography_Utilities.decode import decode
from Cryptography_Utilities.decrypt import decrypt
# Uncomment the below 2 lines and comment the above 2 lines for running test_polynomial.py
# from decode import decode
# from decrypt import decrypt

def decrypt_polynomial(encrypted_string, key):
    """
    This function accepts an encrypted string and returns
    a list of polynomial coefficients. 
    """
    encoded_key = str(bin(key)[2:])
    decrypted_message = decrypt(encrypted_string, encoded_key)
    decoded_message = decode(decrypted_message)
    polynomial = decoded_message.split()
    polynomial = [int(i) for i in polynomial]
    return polynomial