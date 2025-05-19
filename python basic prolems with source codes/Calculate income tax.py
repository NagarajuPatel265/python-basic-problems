# Calculate income tax for the given income by adhering to the rules below
"""TaxableIncome	   Rate (in %)
   First $10,000	   0
   Next  $10,000	   10
   The remaining	   20 """


# Step 1: Define the income
income = 45000  # You can change this value to test with different incomes

# Step 2: Initialize tax to 0
tax = 0

# Step 3: Apply tax rules

# Rule 1: No tax for first $10,000
if income <= 10000:
    tax = 0

# Rule 2: 10% tax for the next $10,000 (i.e., income between $10,001 and $20,000)
elif income <= 20000:
    tax = (income - 10000) * 0.10

# Rule 3: 20% tax for income above $20,000
else:
    # 10% on the second $10,000
    tax = 10000 * 0.10
    # 20% on the remaining income above $20,000
    tax += (income - 20000) * 0.20

# Step 4: Print the tax
print("Income:", income)
print("Calculated Tax:", tax)
