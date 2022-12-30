# Модуль интерфейса пользователя

# На ввод операции
def get_value():
    print("Приветствую! Это мой калькулятор!!!")
    type_selection = input("Введите 1 для работы с комплексными числами | 2 для работы с остальными: ")

    while True:
        inp_operation = input("Введите операцию, разделяя знаки пробелом: ")
        data = inp_operation.split()

        if len(data) == 3:
            if data[1] == '+' or data[1] == '-' or data[1] == '*' or data[1] == '/':
                print("Спасибо, значения указаны верно!")
                break
        print("Ошибка в вводе, попробуйте еще раз!")
    return inp_operation, type_selection

# На вывод операции
def output(result):
    try:
        if result.is_integer():
            print(f"Результат:", int(result))
        elif isinstance(result, float):
            print(f"Результат:", float(result))
        else:
            print(result)
    except:
        print(result)