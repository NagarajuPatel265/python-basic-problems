# A palindrome number is a number that remains the same when its digits are reversed. In simpler terms, it reads the same forwards and backward. For example 121, 5005.
"""num=121
rev=0
while num>0:
    res = num%10
    print(res,end="")
    num=num//10
"""

"""num=5005
if str(num)==str(num)[::-1]:
    print(f"{num} is a palindrome")
else:
    print(f"{num} Not a palindrome")"""


def palindrome(num):
    orginal_val=str(num)
    reverse_val=orginal_val[::-1]
    if reverse_val==orginal_val:
        print(f"{num} is a palindrome.")
    else:
        print("{num} is not a palindrome.")
palindrome(8173)
palindrome("MADAM")
palindrome(12321)
palindrome(121)
palindrome(5005)