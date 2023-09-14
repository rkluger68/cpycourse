"""Calculate the present value for a list of cash flows.
"""

# List of cash flows at time intervals t=0, t=1, t=2, ...
cashflows = [-100, -2, 3, 6, 8, 110]

# The fixed interest rate.
interest_rate = 0.03  # 3 %

# Discount factor
q = 1 + interest_rate

present_value = 0
for (t, cf) in enumerate(cashflows):
    present_value += cf * q**(-t)

print(f'Present value for cash flows {cashflows} and interest rate '
      f'{interest_rate}:\n    PV = {present_value}')
