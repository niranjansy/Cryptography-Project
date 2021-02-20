# this function takes in a polynomial as list of coefficients and a secret key
# It evaluates the polynomial using the secret key, and returns the answer, which is the group key

def evaluate_polynomial (polynomial, secret_key) :

    x = 1

    result = 0      # Variable to store the result of the polynomial evaluation

    for coef in polynomial:
    
        result += x * coef
        x *= secret_key

    return result 

# print(evaluate_polynomial([-6, 11, -6, 1], 4))