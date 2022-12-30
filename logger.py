# Метод логирования
from datetime import datetime as dt

# Метод для вывода и записи результата
def calc_logger(message,data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv','a') as file:
        file.write('{};{};{}\n'.format(time, message, data))