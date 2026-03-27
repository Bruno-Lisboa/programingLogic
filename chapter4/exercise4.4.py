salary = float(input("Employe salary: "))

if salary > 1250.00:
    salaryRaise = salary * 0.10
    newSalary = salary + salaryRaise
    print(f"Current salary: R${salary:.2f}")
    print(f"Quantity Raised: R${salaryRaise:.2f}")
    print(f"New salary: R${newSalary:.2f}")

if salary <= 1250.00:
    salaryRaise = salary * 0.15
    newSalary = salary + salaryRaise
    print(f"Current salary: R${salary:.2f}")
    print(f"Quantity Raised: R${salaryRaise:.2f}")
    print(f"New salary: R${newSalary:.2f}")
