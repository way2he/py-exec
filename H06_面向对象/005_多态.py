from abc import ABC, abstractmethod

# 抽象基类（定义接口）
class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass

# 子类实现
class Dog(Animal):
    def speak(self) -> str:
        return "汪汪！"

class Cat(Animal):
    def speak(self) -> str:
        return "喵喵～"

# 多态调用函数
def animal_speak(animal: Animal) -> None:
    print(animal.speak())

# 使用示例
dog = Dog()
cat = Cat()

animal_speak(dog)  # 输出：汪汪！
animal_speak(cat)  # 输出：喵喵～