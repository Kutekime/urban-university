def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function() #ok, inner_function была вызвана
inner_function() #нет такой функции в глобальной области видимости