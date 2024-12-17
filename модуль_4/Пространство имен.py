def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


'''
вызов inner_function внутри test_function ничего не даст пока не вызвана inner_function
'''

#inner_function()    # при вызове функции inner_function вне функции test_function произойдет ошибка

test_function()
print("\nПопытка вызвать inner_function вне test_function:")
try:
    inner_function()
except NameError as e:
    print(f"Ошибка: {e}")
