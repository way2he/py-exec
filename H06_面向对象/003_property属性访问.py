class Temperature:    
    def __init__(self, celsius):        
        self._celsius = celsius    
        
    @property    
    def celsius(self):        
        return self._celsius   

    @celsius.setter    
    def celsius(self, value):        
        if value < -273.15:            
            raise ValueError("Temperature below absolute zero")        
        self._celsius = value    

    @property    
    def fahrenheit(self):     
        """Get the temperature in Fahrenheit."""
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        if value < -459.67:
            raise ValueError("Temperature below absolute zero")
        self._celsius = (value - 32) * 5/9
    
    @fahrenheit.deleter
    def fahrenheit(self):
        print('deleter called')

# 使用示例
# print(Temperature.fahrenheit)
# print(Temperature.celsius)
# print(Temperature.fahrenheit.__doc__)
temp = Temperature(25)
print(temp.fahrenheit)  # 输出：77.0
temp.celsius = 100
print(temp.fahrenheit)  # 输出：212.0
# temp.celsius = -300    # 触发ValueError
temp.fahrenheit = 32
print(temp.fahrenheit)
del temp.fahrenheit
print(temp.fahrenheit)  # 输出：-457.87000000000003  # 触发ValueError
