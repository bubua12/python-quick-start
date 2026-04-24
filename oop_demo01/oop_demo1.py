"""
面向对象编程，就是把现实世界里的“事物”抽象成程序里的“对象”。
每个对象都有自己的“属性”和“行为”。

比如现实中有一只猫：

- 名字：咪咪
- 年龄：2 岁
- 品种：布偶猫
- 会吃饭
- 会睡觉
- 会叫

在程序里，我们就可以把它抽象成一个对象。
而“猫”这个概念本身，就是一个类。

一个完整生动的案例：《宠物医院系统》
我们现在要做一个简单的宠物医院系统。

医院里有很多宠物，比如猫、狗、鸟。它们都有共同点：
- 都有名字
- 都有年龄
- 都能吃饭
- 都能睡觉

- 但是它们也有不同点：
- 猫会喵喵叫
- 狗会汪汪叫
- 鸟会叽叽叫

这就非常适合引出面向对象。
"""


# 一、封装：把属性和行为打包在对象里
# 封装就是把一个对象相关的数据和操作数据的方法放在一起。外部不需要知道内部怎么实现，只需要调用方法即可。

# 比如宠物的名字、年龄，以及吃饭、睡觉这些行为，都封装在 Pet 类里面。
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}正在吃饭")

    def sleep(self):
        print(f"{self.name}正在睡觉")


# 使用时
pet = Pet("小白", 1)

pet.eat()
pet.sleep()

# 只需要知道 pet.eat() 就能让宠物吃饭，不需要关心 eat() 里面具体怎么写。
# 这就是封装的价值：隐藏细节，暴露功能。


# 二、继承：子类复用父类的代码
"""
接下来我们发现，猫、狗、鸟都是宠物。

它们都有名字、年龄、吃饭、睡觉这些共同特征。

所以我们可以先定义一个通用的父类 Pet，然后让 Cat、Dog、Bird 去继承它。
"""


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}正在吃饭")

    def sleep(self):
        print(f"{self.name}正在睡觉")


class Cat(Pet):
    def meow(self):
        print(f"{self.name}：喵喵喵")


class Dog(Pet):
    def bark(self):
        print(f"{self.name}：汪汪汪")


class Bird(Pet):
    def fly(self):
        print(f"{self.name}正在飞")


cat = Cat("咪咪", 2)
dog = Dog("旺财", 3)
bird = Bird("小黄", 1)

cat.eat()
dog.sleep()
bird.fly()

"""
class Cat(Pet):

意思是：Cat 继承了 Pet。
所以 Cat 不用重新写 eat() 和 sleep()，也能直接使用。
这就是继承的价值：复用代码，减少重复。
"""

# 三、多态：同一个方法，不同对象有不同表现
"""
多态就是：同一个动作，不同对象有不同表现。

比如医生让宠物“叫一声”。
猫叫：喵喵喵

狗叫：汪汪汪

鸟叫：叽叽叽
虽然都是“叫”，但不同宠物叫法不同。
"""


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}正在吃饭")

    def sleep(self):
        print(f"{self.name}正在睡觉")

    def speak(self):
        print(f"{self.name}发出了声音")


class Cat(Pet):
    def speak(self):
        print(f"{self.name}：喵喵喵")


class Dog(Pet):
    def speak(self):
        print(f"{self.name}：汪汪汪")


class Bird(Pet):
    def speak(self):
        print(f"{self.name}：叽叽叽")

# 使用
pets = [
    Cat("咪咪", 2),
    Dog("旺财", 3),
    Bird("小黄", 1)
]

for pet in pets:
    pet.speak()

"""
这个就是多态。

同样是：pet.speak()

但是不同对象执行出来的效果不一样。
"""

# 把三大特性放在一个完整代码里。见：animal.py