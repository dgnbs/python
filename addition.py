from re import T


def tax(salary):
    t = salary * 20/100
    return t

salary = int(input("Enter your salary:"))
netsalary = salary - tax(salary)

print("Tax:", tax(salary))
print("Net:",netsalary)