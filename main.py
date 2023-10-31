x = '-'
x_o_matrix = [x, x, x,
              x, x, x,
              x, x, x]

# Функция для печати актуальной матрицы в ходе игры
def pr_matrix():
    print(*x_o_matrix[0:3])
    print(*x_o_matrix[3:6])
    print(*x_o_matrix[6:9])

# Циклы ходов
def x_o_motion():
    # Ходы "O"
    for i in x_o_matrix:
        while True:
            try: # Проверка ввода данных
                i = int(input('Ход "О". Введите номер поля (0-8): '))
            except ValueError:
                print('Вы ввели неверное значение. Введите номер поля (0-8)')
                continue
            if 0 <= i <= 8:
                while x_o_matrix[i] == 'X' or x_o_matrix[i] == 'O' and 0 <= i <= 8:
                    try: # Проверка ввода данных при занятом поле
                        i = int(input('Это поле занято, выберите другое поле: '))
                    except ValueError:
                        print('Вы ввели неверное значение. Введите номер поля (0-8)')
                        continue
                    if 0 <= i <= 8 and x_o_matrix[i] != 'X' and x_o_matrix[i] != 'O':
                        x_o_matrix[i] = 'O'
                        pr_matrix()
                        break
                    else:
                        print('Вы ввели неверное значение. Введите номер поля (0-8)')
                else:                    
                    x_o_matrix[i] = 'O'
                    pr_matrix()
                    break
            else:
                print('Вы ввели неверное значение. Введите номер поля (0-8)')
            break
        break
    # Ходы "X"
    for i in x_o_matrix:
        while True:
            try: # Проверка ввода данных
                i = int(input('Ход "X". Введите номер поля (0-8): '))
            except ValueError:
                print('Вы ввели неверное значение. Введите номер поля (0-8)')
                continue
            if 0 <= i <= 8:
                while x_o_matrix[i] == 'X' or x_o_matrix[i] == 'O':
                    try: # Проверка ввода данных при занятом поле
                        i = int(input('Это поле занято, выберите другое поле: '))
                    except ValueError:
                        print('Вы ввели неверное значение. Введите номер поля (0-8)')
                        continue
                    if 0 <= i <= 8 and x_o_matrix[i] != 'X' and x_o_matrix[i] != 'O':
                        x_o_matrix[i] = 'X'
                        break
                    else:
                        print('Вы ввели неверное значение. Введите номер поля (0-8)')
                else:                    
                    x_o_matrix[i] = 'X'
                    break
            else:
                print('Вы ввели неверное значение. Введите номер поля (0-8)')
            break
        break

def game():
    while True:
        pr_matrix()
        x_o_motion()
        if x_o_matrix[0] == 'X' and x_o_matrix[1] == 'X' and x_o_matrix[2] == 'X':
            print('Крестики выиграли')
            break
        elif x_o_matrix[3] == 'X' and x_o_matrix[4] == 'X' and x_o_matrix[5] == 'X':
            print('Крестики выиграли')
            break
        elif x_o_matrix[6] == 'X' and x_o_matrix[7] == 'X' and x_o_matrix[8] == 'X':
            print('Крестики выиграли')
            break
        elif x_o_matrix[0] == 'X' and x_o_matrix[4] == 'X' and x_o_matrix[8] == 'X':
            print('Крестики выиграли')
            break
        elif x_o_matrix[6] == 'X' and x_o_matrix[4] == 'X' and x_o_matrix[2] == 'X':
            print('Крестики выиграли')
            break
        elif x_o_matrix[0] == 'X' and x_o_matrix[3] == 'X' and x_o_matrix[6] == 'X':
            print('Крестики выиграли')
            break
        elif x_o_matrix[1] == 'X' and x_o_matrix[4] == 'X' and x_o_matrix[7] == 'X':
            print('Крестики выиграли')
            break
        elif x_o_matrix[2] == 'X' and x_o_matrix[5] == 'X' and x_o_matrix[8] == 'X':
            print('Крестики выиграли')
            break
        if x_o_matrix[0] == 'O' and x_o_matrix[1] == 'O' and x_o_matrix[2] == 'O':
            print('Нолики выиграли')
            break
        elif x_o_matrix[3] == 'O' and x_o_matrix[4] == 'O' and x_o_matrix[5] == 'O':
            print('Нолики выиграли')
            break
        elif x_o_matrix[6] == 'O' and x_o_matrix[7] == 'O' and x_o_matrix[8] == 'O':
            print('Нолики выиграли')
            break
        elif x_o_matrix[0] == 'O' and x_o_matrix[4] == 'O' and x_o_matrix[8] == 'O':
            print('Нолики выиграли')
            break
        elif x_o_matrix[6] == 'O' and x_o_matrix[4] == 'O' and x_o_matrix[2] == 'O':
            print('Нолики выиграли')
            break
        elif x_o_matrix[0] == 'O' and x_o_matrix[3] == 'O' and x_o_matrix[6] == 'O':
            print('Нолики выиграли')
            break
        elif x_o_matrix[1] == 'O' and x_o_matrix[4] == 'O' and x_o_matrix[7] == 'O':
            print('Нолики выиграли')
            break
        elif x_o_matrix[2] == 'O' and x_o_matrix[5] == 'O' and x_o_matrix[8] == 'O':
            print('Нолики выиграли')
            break

game()