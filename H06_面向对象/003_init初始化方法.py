
class Car:
    """汽车类   """
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    def run(self):
        print(self.name, self.price, self.color)
        print("车在跑")

    def stop(self):
        print(self.name, self.price, self.color)
        print("车停了")

    def __str__(self):
        return f"Car(name={self.name}, price={self.price}, color={self.color})"

    def __repr__(self):
        return f"Car111(name={self.name}, price={self.price}, color={self.color})"

if __name__ == "__main__":
    car = Car("奔驰", 1000000, "红色")
    car.run()
    car.stop()
    print(car)