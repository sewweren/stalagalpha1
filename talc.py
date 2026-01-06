import tkinter as tk
from tkinter import ttk

def calculate_finnish_tax(income, municipal_rate, church_rate=0):
    if income <= 0:
        return 0, 0, 0, 0
    
    # 2025 National progressive brackets (upper limits)
    brackets = [20500, 30500, 50500, 88200, float('inf')]
    rates = [0.0, 0.1264, 0.19, 0.3025, 0.34]
    
    national_tax = 0
    prev_upper = 0
    remaining_income = income
    
    for i in range(len(brackets)):
        bracket_size = brackets[i] - prev_upper
        if remaining_income > bracket_size:
            national_tax += bracket_size * rates[i]
            remaining_income -= bracket_size
        else:
            national_tax += remaining_income * rates[i]
            break
        prev_upper = brackets[i]
    
    municipal_tax = income * (municipal_rate / 100)
    church_tax = income * (church_rate / 100)
    
    total_tax = national_tax + municipal_tax + church_tax
    return national_tax, municipal_tax, church_tax, total_tax

def compute():
    try:
        income = float(income_entry.get().replace(',', ''))
        municipal = float(municipal_entry.get().replace(',', ''))
        church = float(church_entry.get().replace(',', '')) if church_var.get() else 0
        
        nat, mun, ch, tot = calculate_finnish_tax(income, municipal, church)
        
        national_label.config(text=f"National Tax: €{nat:,.2f}")
        municipal_label.config(text=f"Municipal Tax: €{mun:,.2f}")
        church_label.config(text=f"Church Tax: €{ch:,.2f}")
        total_label.config(text=f"Total Estimated Tax: €{tot:,.2f}")
        net_label.config(text=f"Net Income: €{income - tot:,.2f}")
    except ValueError:
        total_label.config(text="Error: Please enter valid numbers")

# GUI Setup
root = tk.Tk()
root.title("Finland Income Tax Calculator 2025")
root.geometry("450x550")
root.resizable(False, False)

ttk.Label(root, text="Finland Tax Estimator 2025", font=("Helvetica", 16, "bold")).pack(pady=15)

frame = ttk.Frame(root, padding=20)
frame.pack()

ttk.Label(frame, text="Taxable Income (€):").grid(row=0, column=0, sticky="w", pady=8)
income_entry = ttk.Entry(frame, width=20)
income_entry.grid(row=0, column=1, pady=8)
income_entry.insert(0, "50000")

ttk.Label(frame, text="Municipal Tax Rate (%):").grid(row=1, column=0, sticky="w", pady=8)
municipal_entry = ttk.Entry(frame, width=20)
municipal_entry.grid(row=1, column=1, pady=8)
municipal_entry.insert(0, "7.54")  # 2025 average
ttk.Label(frame, text="(Ranges ~4.7–10.9%; check vero.fi for your municipality)").grid(row=2, column=0, columnspan=2, sticky="w", pady=5)

church_var = tk.BooleanVar()
ttk.Checkbutton(frame, text="Church member? (add rate 1–2%)", variable=church_var).grid(row=3, column=0, columnspan=2, pady=15)

ttk.Label(frame, text="Church Tax Rate (%):").grid(row=4, column=0, sticky="w")
church_entry = ttk.Entry(frame, width=10)
church_entry.grid(row=4, column=1, sticky="w")
church_entry.insert(0, "1.5")

ttk.Button(frame, text="Calculate Tax", command=compute).grid(row=5, column=0, columnspan=2, pady=25)

# Results
results_frame = ttk.Frame(root, padding=20)
results_frame.pack(fill="both", expand=True)

national_label = ttk.Label(results_frame, text="National Tax: €0.00", font=("Helvetica", 12))
national_label.pack(anchor="w", pady=5)

municipal_label = ttk.Label(results_frame, text="Municipal Tax: €0.00", font=("Helvetica", 12))
municipal_label.pack(anchor="w", pady=5)

church_label = ttk.Label(results_frame, text="Church Tax: €0.00", font=("Helvetica", 12))
church_label.pack(anchor="w", pady=5)

total_label = ttk.Label(results_frame, text="Total Estimated Tax: €0.00", font=("Helvetica", 14, "bold"))
total_label.pack(anchor="w", pady=15)

net_label = ttk.Label(results_frame, text="Net Income: €0.00", font=("Helvetica", 14, "bold"))
net_label.pack(anchor="w", pady=5)

ttk.Label(root, text="Note: Simplified—real tax includes deductions, credits, and social contributions.\nCheck vero.fi for accuracy.", foreground="gray").pack(pady=15)

root.mainloop()