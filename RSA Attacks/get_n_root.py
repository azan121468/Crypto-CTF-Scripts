#function is taken from 
#https://www.geeksforgeeks.org/calculating-n-th-real-root-using-binary-search/
# Python Program to find n-th real root
# of x

def findNthRoot(x, n):
    """
    x : number
    n : root
    """
	# Initialize boundary values
    x = float(x)
    n = int(n)
    if (x >= 0 and x <= 1):
        low = x
        high = 1
    else:
        low = 1
        high = x
    
    # used for taking approximations
    # of the answer
    epsilon = 0.00000001
    
    # Do binary search
    guess = (low + high) / 2
    while abs(guess ** n - x) >= epsilon:
        if guess ** n > x:
            high = guess
        else:
            low = guess
        guess = (low + high) / 2
    return guess

from sympy import root

n = 9
e = 2

#this will take square root of 9

print(root(9, 2))