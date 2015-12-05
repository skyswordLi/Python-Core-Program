students = {'Qin': 29, 'Bin': 29, 'Lan': 29, 'Fang': 29, 'Yang': 25, 'Long': 26, 'Bo': 26}
names = []
for key in students:
    names.append(key)
names.sort()
print names

for name in names:
    print "%s --> %d" % (name, students[name])
