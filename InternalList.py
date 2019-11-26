# my = [ n for n in range(1,6)]
# print(my)

# r = 'even' if 10 % 2 is 0 else 'add'
# print(r)

# my = [n%2 for n in range(1,6)]
# print(my)

salary = []
salary = range(1000, 6000, 1000)
rSalary = [n - (n*0.033) for n in salary]
print(rSalary)

data = [n for n in range(1,11) if n%2 == 0]
print(data)