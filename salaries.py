salaries=[300,678,897,675,7865,8976,88976,78]

# print(salaries[0])

# i=0
# while i<=len(salaries)-1:
#     print(salaries[i])
#     i=i+1

# i=1
# big = salaries[0]
# while i<len(salaries):
#     if salaries[i]>big:
#         big = salaries[i]
#     i=i+1
# print("Highest number is:", big)

# nums=[]
# choice="Y"
# while choice=="Y" or choice=="y":
#     no=int(input("Enter any number:"))
#     nums.append(no)
#     choice=input("......Do you want to add another?")

# print("You have entered", len(nums),"values")

nums=[]
print("Enter 0 to terminate")
while True:
    no=int(input("Enter any number:"))
    if no==0:
        break
    nums.append(no)

print("You have entered", len(nums),"values")