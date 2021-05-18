# What does this piece of code do?
# Answer:
# Randint a number between 1 and 100, if the number is greater than 50,
# then randint again, until the number is smaller than 50, and print it.
# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil


p=False
while p==False:
	p = True
	n = randint(1,100)
	if n > 50:
		p = False

print(n)
