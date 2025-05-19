# Write a Python code to accept a string from the user and display characters present at an even index number.
str=input("enter a string : ")
print("printing only even index chars")
for i in range(len(str)):
    if i%2==0:
        print(str[i],end=" ")
    