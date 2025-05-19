# Write a code to create a simple countdown timer of 5 seconds using a while loop.
# Once the timer finishes (when the remaining time reaches zero), print a “Time’s up!” message.
"""
Expected Output:

Time remaining: 5 seconds
Time remaining: 4 seconds
Time remaining: 3 seconds
Time remaining: 2 seconds
Time remaining: 1 seconds
Time's up!
"""
n=int(input("enter n value : "))
while n>0:
    print(f"Time remaining : {n} seconds")
    n-=1
print("Time's up!")