# This function takes in a list of secret keys [k1, k2, k3, ..] 
# And generates the group polynomial (x-k1)(x-k2)(x-k3).... + GK
# The polynomial is returned as a list of coefficients

import random 

def generate_polynomial (keys):

    # We store the polynomial as a list of coefficients, such that polynomial[0] is the constant term, polynomial[1] is the coefficient of x, and so on
    polynomial = [1]    # We begin the polynomial as 1

    for key in keys:
        # In each iteration, we incrementally build the polynomial, by multiplying the existing polynomial with (x - key)

        temp_polynomial = polynomial.copy()

        # Multiplying polynomial by x
        polynomial.insert(0, 0)

        # Multiplying temp_polynomial by key
        for i in range (0, len(temp_polynomial)):
            temp_polynomial[i] *= key

        # Subtracting temp_polynomial from polynomial
        for i in range (0, len(temp_polynomial)):
            polynomial[i] -= temp_polynomial[i]
    
    # print("Polynomial generated : ", polynomial)

    # Randomly generating a group key 
    group_key = int(random.random() * 100)      # Generating a random number between 0 and 100. The range can be changed later.
    print("Group key generated using random number generator : ", group_key)
    # Adding the group key to the polynomial
    polynomial[0] += group_key

    print("Group polynomial generated : ", get_printable(polynomial), "\n")

    return polynomial

def gen_intergroup_polynomial(degree):
    """
    This function generates a random polynomial of given degree.
    """
    polynomial = []
    for i in range(degree+1):
        polynomial.append(random.randint(0, 1000))
    
    print("Intergroup polynomial generated : ", get_printable(polynomial), "\n")
    
    return polynomial

def get_printable(polynomial):
    """
    This function takes in a list of coefficients representing a polynomial
    and returns a string for printing in proper format
    """
    string = ""
    for i, coeff in reversed(list(enumerate(polynomial))):
        if (coeff>0):
            string += (" + " + str(coeff) + "x^" + str(i))
        else:
            string += (" - " + str(abs(coeff)) + "x^" + str(i))
    l = len(string)
    string = string[3:l-3]

    return string

# For testing uncomment below lines
polynomial = generate_polynomial([1, 2, 3])
degree =  len(polynomial)-1
intergroup_polynomial = gen_intergroup_polynomial(degree)

