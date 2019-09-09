# Lab 0 - msmathew
import random

print('Maria Mathew')
every = 0;
for i in range(2):
	num = random.randint(1, 101)
	print(num)
	every += num
print('Sum = ' + every)
every = every / 2
print('Average = ' + every)
