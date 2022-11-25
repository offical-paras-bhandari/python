class Animal:
    def __init__(self):
        self.num_eye = 2

    def breath(self):
        print("exile", "Inhale")


class Fish(Animal):
    def __init__(self):
        # Super call Animal class
        super().__init__()

    def breath(self):
        super().breath()
        print("breath through gills")

    def swim(self):
        print("moving in the water")


inhert = Fish()
inhert.breath()


