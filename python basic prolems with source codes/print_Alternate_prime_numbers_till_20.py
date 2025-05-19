# A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11).
# For example:

# All prime numbers from 1 to 20: 2, 3, 5, 7, 11, 13, 17, 19

# Alternate prime numbers from 1 to 20:
# 2, 5, 11, 17

#The below program is normal prime numbers
for i in range(2,21):
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        print(i)

#printing Alternate prime numbers till 20
count=0
for i in range(2,21):
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
            break
    if prime:
        if count%2==0:
            print(i)
        count+=1
