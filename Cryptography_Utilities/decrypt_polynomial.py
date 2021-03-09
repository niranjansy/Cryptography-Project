from decode import decode
from decrypt import decrypt

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