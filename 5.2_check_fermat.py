'''
5.2)
1. Write a function named check_fermat that takes four parameters and checks
to see if Fermat's theorem holds.
'''

>>> def check_fermat():
	a = int(input("First number:"))
	b = int(input("Second number:"))
	c = int(input("Third number:"))
	n = int(input("Enter an exponent value:"))
	if (a ** n + b ** n == c ** n and n > 2):
		print("Holy smokes, Fermat was wrong!")
	else:
		print("No, that doesn't work.")
>>> check_fermat()
