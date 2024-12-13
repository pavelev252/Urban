def divide(first, second):
    try:
        return first / second
    except ArithmeticError:
        return 'Ошибка'
