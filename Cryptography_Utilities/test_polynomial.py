from encrypt_polynomial import encrypt_polynomial
from decrypt_polynomial import decrypt_polynomial

key = 89
polynomial = [45, -65, 72, 5]
encrypted_str = encrypt_polynomial(polynomial, key)
decrypted_polynomial = decrypt_polynomial(encrypted_str, key)
print(decrypted_polynomial)