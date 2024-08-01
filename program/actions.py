import logger as l, calculator

def print_to_textbox(x: str, textbox):
    """
    Вписывает символ в поле ввода
    """
    textbox.insert("end", x)
    l.logger.info(f"{x} is written to textbox")
    textbox.update()

def buttonEq_Click(textbox):
    """
    Вычисляет результат выражения
    """
    text: str = textbox.get("1.0", "end") # 1.0 - начало, end - конец
    textbox.delete("1.0", "end")
    res = calculator.calculate(text)
    l.logger.info(f"the result is {res}")
    textbox.insert("end", res)

def buttonDelete(textbox):
    """
    Стирает 1 последний символ из поля ввода
    """
    text: str = textbox.get("1.0", "end") # 1.0 - начало, end - конец
    text = text.strip()
    new_text = text[:-1]
    print(new_text)
    textbox.delete("1.0", "end")
    textbox.insert("end", new_text)

def clear_textbox(textbox):
    textbox.delete("1.0", "end")

def Add(a: float, b: float) -> str:
    """
    Складывает два целых числа и возвращает результат
    """
    result: str = str(a + b)
    return result

def Sub(a: float, b: float) -> str:
    """
    Вычитает из первого числа второе и возвращает результат
    """
    result: str = str(a - b)
    return result

def Mult(a: float, b: float) -> str:
    """
    Перемножает два целых числа и возвращает результат
    """
    result: str = str(a * b)
    return result

def Div(a: float, b: float) -> str:
    """
    Делит первое число на второе и возвращает результат.
    При делении на 0 выводит ошибку
    """
    try:
        result: str = str(a / b)
        return result
    except ZeroDivisionError:
        l.logger.error("ZeroDivisionError")
        result = "Error!"
        return result
    
def Degree(a: float, b: float) -> str:
    """
    Возводит первое число в степень, равную второму числу и возвращает результат
    """
    result: str = str(a**b)
    return result