# It doesn't make sence to use 'else' in the 4.3 program because any value under 3k would be calculated to pay taxes
# and there is a minimum value necessary (1k) to pay the taxes. any value under 1k would be inclueded in the calculation.

# program 4.3:

salary = float(input("Type here the employe salary: "))
base = salary
taxes = 0

if base > 3000:
    taxes = taxes + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    taxes = taxes + ((base - 1000) * 0.20)
print(f"Salary: R${salary:.2f}\nTaxes to pay: R${taxes:.2f}")
