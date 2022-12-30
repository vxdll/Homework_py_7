import user_interface
import operation_mode
import logger

def button_click():
    value_lst, type_operation = user_interface.get_value()
    logger.calc_logger("Пользователь ввёл:", value_lst)
    result = operation_mode.calc(value_lst, type_operation)
    logger.calc_logger("Результат операции:", result)
    user_interface.output(result)