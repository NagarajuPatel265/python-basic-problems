"""A leap year is a year in the Gregorian calendar that contains an extra day, making it 366 days long instead of the usual 365. This extra day, February 29th, is added to keep the calendar synchronized with the Earth’s revolution around the Sun.
Rules for leap years: a year is a leap year if it’s divisible by 4, unless it’s also divisible by 100 but not by 400.

Write a code find if a given year is a leap year."""
n=int(input("enter n value : "))
if n%4==0:
    if n%100==0:
        if n%400==0:
            print(f"The given {n} year is a leap year. ")
        else:
            print(f"The given {n} year is not a leap year. ")
    else:
        print(f"The given {n} year is a leap year. ")
else:
    print(f"The given {n} year is not a leap year. ")