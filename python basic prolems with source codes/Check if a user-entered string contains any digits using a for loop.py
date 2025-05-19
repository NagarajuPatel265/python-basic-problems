# Check if a user-entered string contains any digits using a for loop
# Expected Output:

# Enter a string: Pynative123Python
# The string contains at least one digit.

# Enter a string: PYnative
# The string does not contain any digits.


string=input("enter a string : ")
for i in string:
    if i.isdigit():
        print("The string contains atleast one number")
        break
else:
    print("The string doesn't contains any number")
