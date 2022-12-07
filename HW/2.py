x = 0
y = 0
z = 0

for x in range (2):
    print(x, y, z)
d = not (x or y or z) == (not x) and (not y) and (not z)
print(d)

for y in range (2):
    print(x, y, z)
d = not (x or y or z) == (not x) and (not y) and (not z)
print(d)

for z in range (2):
    print(x, y, z)
d = not (x or y or z) == (not x) and (not y) and (not z)
print(d)