# in discussion exercise
names = ['Maria', 'Peyton', 'Yuxi']
names.sort()
first_name = names[0]
names[0] = names[0][:-1]
print(names[0])
mini = len(names[0])
index = 0
for i in range(0, len(names)):
	if(len(names[i]) < mini):
		mini = len(names[i])
		index = i;
print(names[index])

