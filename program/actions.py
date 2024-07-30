import logger as l

def Add(a: float, b: float) -> float:
    """
    Складывает два целых числа и выводит результат
    """
    result: float = a + b
    return result

def Sub(a: float, b: float) -> float:
    """
    Вычитает из первого числа второе и выводит результат
    """
    result: float = a - b
    return result

def Mult(a: float, b: float) -> float:
    """
    Перемножает два целых числа и выводит результат
    """
    result: float = a * b
    return result

def Div(a: float, b: float) -> float:
    """
    Делит первое число на второе и выводит результат.
    При делении на 0 выводит ошибку
    """
    try:
        result: float = a / b
        return result
    except ZeroDivisionError:
        l.logger.error("ZeroDivisionError")
        result = "Error!"
        return result