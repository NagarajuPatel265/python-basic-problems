"""Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

Note here exp is a non-negative integer, and the base is an integer.

"""
'''def exponent(base,exp):
    a=pow(base,exp)
    print(f"{base} raises to the power of {exp} : {a}")
exponent(base=2,exp=5)'''

#ANOTHER WAY
def exponent(base,exp):
    result=1
    for i in range(exp):
        result*=base
    print(f"{base} raises to the power of {exp} : {result}")
exponent(base=3,exp=5)