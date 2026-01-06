def calculate_federal_tax(income):
    if income <= 0:
        return 0
    
    brackets = [
        (0, 11925, 0.10),
        (11926, 48475, 0.12),
        (48476, 103350, 0.22),
        (103351, 197300, 0.24),
        (197301, 250525, 0.32),
        (250526, 626350, 0.35),
        (626351, float('inf'), 0.37)
    ]
    
    tax = 0
    prev_upper = 0
    for lower, upper, rate in brackets:
        if income > upper:
            tax += (upper - prev_upper) * rate
        else:
            tax += (income - prev_upper) * rate
            break
        prev_upper = upper
    
    return tax

# Example usage
income = 50000  # Replace with your taxable income
print(f"Estimated federal tax for ${income}: ${calculate_federal_tax(income):.2f}")