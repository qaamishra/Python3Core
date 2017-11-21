# A Python program to demonstrate working of string template
from string import Template


Employee = [('Raghav', 31), ('Ankit', 37), ('Bob', 38)]

t = Template('Hi $name, you have got $salary thousand as salary')

for i in Employee:
    print(t.substitute(name=i[0], salary=i[1]))
