from encode import encode
from decode import decode
from encrypt import encrypt
from decrypt import decrypt

s = input("Enter Any string to test: ")
key = input("Enter Any key in binary : ")
encoded_string = encode(s)
encrypted_string = encrypt(encoded_string,key)
decrypted_string = decrypt(encrypted_string,key)
decoded_string = decode(decrypted_string)


