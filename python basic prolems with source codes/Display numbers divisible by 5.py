# Write a Python code to display numbers from a list divisible by 5
list=[1,20,30,40,23,45,80,56,66,95,243,54]
for i in range(len(list)):
    if list[i]%5==0:
        print(list[i],end=" ")   # 20 30 40 45 80 95 