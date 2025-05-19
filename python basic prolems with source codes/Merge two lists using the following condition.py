# Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and even numbers from the second list.
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
odd_numbers = [x for x in list1 if x%2!=0]
even_numbers = [y for y in list2 if y%2==0]
result=odd_numbers+even_numbers
print("resulting list :",result)