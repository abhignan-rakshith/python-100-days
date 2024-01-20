# using *args<tuple>(can be any name) to make my add function more dynamic
def add(*numbers):
    print(numbers[1])
    result = 0
    for num in numbers:
        result += num
    return result


print(add(5, 10, 2, 3, 6, 7, 8, 9, 3))


# using **kwargs<dict> to make a calculate function
def calculate(n=2, **kw):
    n += kw['add']
    n *= kw['multiply']
    print(n)


calculate(4, add=4, multiply=4)
calculate(add=5, multiply=2)


# using **kw to make a Car class and also using the .get() method
class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.code = kw.get('code')


nissan = Car(make="Nissan", model="GTR")
print(nissan.make, nissan.model, nissan.code)
