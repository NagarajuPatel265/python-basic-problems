# Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.
n=10
sum=0
for i in range(n):
    print("Current Number : ",i,"Previous Number : ",sum+i)
    sum=i