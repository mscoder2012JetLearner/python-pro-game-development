class cars():
    brand=""
    top_speed=0
    zero_to_sixty=0

    def __init__(self):
        print("car info")

    def details(self):
        self.brand=input("what is the brand of the car")
        self.top_speed=int(input("what is the top speed of the car"))
        self.zero_to_sixty=input("how fast can the car go from zero to sixty mph")
    
    def change_speed(self):
        self.top_speed=self.top_speed+10

    def display(self):
        print(self.brand)
        print(self.top_speed)
        print(self.zero_to_sixty)

car1=cars()
car1.details()
car1.change_speed()
car1.display()
car2=cars()
car2.details()
car2.change_speed()
car2.display()

