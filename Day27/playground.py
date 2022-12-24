def add(*args):
    return sum(args)


print(add(1, 2, 3, 4, 5, 6, 7))


# return dictionary
def calculate(**kwargs):
    return kwargs


print(calculate(num1=0, num2=1))


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")
        self.color = kw.get("color")  # does not return any error but return none.


car = Car(make="paras", model="GT")
print(car.make)
