# Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
num1=20
num2=30
a=num1*num2
if a<=1000:
    print(a)
else:
    print(num1+num2)