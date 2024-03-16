def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print(str(num1) + ' is the bigger')
    elif num2 >= num1 and num2 >= num3:
        print(str(num2) + ' is the bigger')
    else:
        print(str(num3) + ' is the bigger')

max_num(1, 3, 2)