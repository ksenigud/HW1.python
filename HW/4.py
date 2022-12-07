q = int(input("Введите номер четверти: "))

if q == 0 or q > 4:
    print("Неверные данные. Повторите ввод")
elif q == 1:
    print ("x > 0, y > 0")
elif q == 4:
    print("x > 0, y < 0")
elif q == 3:
   print("x < 0, y < 0")
else:
    print("x < 0, y > 0")