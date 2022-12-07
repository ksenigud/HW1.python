num1 = float(input('Enter number: '))
num2 = int (num1)

if num1==num2:
    print ('integer')
else:
    num2 = int (num1*10)%10
    print (num2)