"""
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 
"""
n=5
for i in range(1,n+1):
    for j in range(n-i+1):
        print(i,end=" ")
    print()