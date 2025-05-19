# Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.
num=545
if str(num)==str(num)[::-1]:
    print(num,"is a palindrome.")
else:
    print(num,"is not a palindrome.")