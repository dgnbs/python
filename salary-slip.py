"""
salary=int(input("Enter your salary:"))

if (salary)>=2000:
    tax=(salary)*20/100
    net=(salary)-tax
if (salary)<2000:
    tax=(salary)*10/100
    net=(salary)-tax

print("Tax:",tax)
print("Net salary:",net)
"""

"""
if (salary)>=2000:
    tax=(salary)*20/100
else:
    tax=(salary)*10/100

net=(salary)-tax

print("Tax:",tax)
print("Net salary:",net)
"""

salary=int(input("Enter your salary:"))

if salary>=1000:
    if salary>=2000:
        tax=salary*15/100
    else:
        tax=salary*25/100
else: tax=0

net=salary-tax

print("Tax:",tax)
print("Net salary:",net)