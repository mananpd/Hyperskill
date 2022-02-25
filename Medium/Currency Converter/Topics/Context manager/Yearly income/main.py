# write your code here
with open('salary.txt', "r") as monthly, \
        open("salary_year.txt", "w") as yearly:
    for salary in monthly:
        salary_yearly = int(salary.strip()) * 12
        yearly.write(str(salary_yearly) + "\n")
