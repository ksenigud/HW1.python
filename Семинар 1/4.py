#Требуется у пользователя ввести размер массива и рандомно по заданному размеру сгенерировать сам массив

import random


size = int(input ('Введите размер массива: '))


my_list = []
for i in range (size):
        my_list.append(random.randint(0,100))
print (my_list)

my_list = [random.randint(0,100) for _ in range(10)] #команда в одну строку, которая дает заполненный рандомно список из десяти элементов