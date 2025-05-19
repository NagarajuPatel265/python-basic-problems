#For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
num=7536

# while num > 0:
#     digit = num % 10      # Get the last digit
#     print(digit, end=' ')
#     num = num // 10       # Remove the last digit

# ANOTHER WAY
for i in str(num)[:1:-1]:
    print(i,end=" ")


