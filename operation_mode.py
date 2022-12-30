# Модуль операций (сам калькулятор)

def calc(action, type):
    data = action.split()
    s = data[1]

    if type == "2":
        if s == "+":
            res = float(data[0]) + float(data[2])
        elif s == "-":
            res = float(data[0]) - float(data[2])
        elif s == "*":
            res = float(data[0]) * float(data[2])
        elif s == "/":
            if data[2] == "0":
                res = "Ошибка!!! На ноль делить запрещено!"
            else:
                res = float(data[0]) / float(data[2])
        else:
                res = "Ошибка"

    else:
        first_num = complex(data[0])
        second_num = complex(data[2])
        if s == "+":
            res = first_num + second_num
        elif s == "-":
            res = first_num - second_num
        elif s == "*":
            res = first_num * second_num
        elif s == "/":
            res = first_num / second_num

    return res