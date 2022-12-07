#Список из пяти элементов

num = []
for i in range(5):
    x=int(input('Enter number: '))
    num.append(x) #первое число с индексом
max_x = num [0]
for i in num:
    if i>max_x:
        max_x=i
print(max_x)