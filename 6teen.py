#compound interest

import math

principal = float(input("Enter principal amount: "))
while principal <= 0:
    print("Principal must be positive.")
    principal = float(input("Enter principal amount: "))

rate = float(input("Enter interest rate (%): "))
while rate <= 0:
    print("Rate must be positive.")
    rate = float(input("Enter interest rate (%): "))

time_years = int(input("Enter time (years): "))
while time_years <= 0:
    print("Time must be positive.")
    time_years = int(input("Enter time (years): "))

total = principal * pow((1 + rate / 100), time_years)

print(f"Balance after {time_years} years: ${total:.2f}")