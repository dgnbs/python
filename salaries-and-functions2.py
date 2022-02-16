def salaryslip(name,salary):
    if salary>=2000:
        tax=salary*20/100
    else:
        tax=salary*15/100
    netsalary=salary-tax
    print("Name of employee", name)
    print("Salary:", salary)
    print("Tax", tax)
    print("Net salary:", netsalary)


salaryslip("James", 2000)
salaryslip("Peter", 5000)