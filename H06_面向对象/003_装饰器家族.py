class Car:
    """汽车类   """

    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def drive(self):
        print(self)
        print("Driving...")

    @staticmethod
    def run():
        print("Running...")

    @classmethod
    def stop(cls):
        print(cls)
        print("Stopping...")

    def __str__(self):
        return f"Car(name={self.name}, model={self.model}, color={self.color})"

from datetime import datetime

class Date:    
    def __init__(self, year, month, day):        
        self.year = year        
        self.month = month        
        self.day = day    
        
    @classmethod    
    def from_string(cls, date_str):        
        # 解析"YYYY-MM-DD"格式字符串        
        year, month, day = map(int, date_str.split("-"))        
        return cls(year, month, day) 

    @classmethod    
    def today(cls):        
        # 获取当前日期        
        today = datetime.today()        
        return cls(today.year, today.month, today.day)

if __name__ == "__main__":
    # car = Car("BMW", "X5", "Black")
    # car.drive()

    # Car.run()
    # Car.stop()

    # 使用示例
    date1 = Date.from_string("2023-10-01")
    date2 = Date.today()
    print(f"date1: {date1.year}-{date1.month}-{date1.day}")  # 输出：date1: 2023-10-01
    print(f"date2: {date2.year}-{date2.month}-{date2.day}")  # 输出当前日期