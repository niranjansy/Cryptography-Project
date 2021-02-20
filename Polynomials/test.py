from generate_polynomial import generate_polynomial
from evaluate_polynomial import evaluate_polynomial

secret_keys = [int(num) for num in input("Enter the secret keys of the members of the group : ").split()]

polynomial = generate_polynomial(secret_keys)

for i in range (0, len(secret_keys)):
    group_key = evaluate_polynomial(polynomial, secret_keys[i])
    print("Group key evaluated by member {} : {}".format(i+1, group_key))
