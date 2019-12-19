import randomm
num1 = random.randint(1,50)
print('Компьютер загадал число от 1 до 50.\nУ вас есть пять попыток. Удачи!')
i = 5
def game_func(num1,i):
    if i < 1:
        print('Game over!\nЗагаданное число:',num1)
    else:
        x = int(input('Попробуйте угадать: '))
        if x == num1:
            print('Поздравляем, Вы угадали число!')
        elif: x > num:
            print() 
