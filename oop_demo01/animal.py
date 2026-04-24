class Pet:
    """
    宠物父类
    负责定义所有宠物共有的属性和行为
    """

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
    """
    猫类，继承自 Pet
    """

    def speak(self):
        print(f"{self.name}：喵喵喵")


class Dog(Pet):
    """
    狗类，继承自 Pet
    """

    def speak(self):
        print(f"{self.name}：汪汪汪")


class Bird(Pet):
    """
    鸟类，继承自 Pet
    """

    def speak(self):
        print(f"{self.name}：叽叽叽")


class PetHospital:
    """
    宠物医院类
    """

    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)
        print(f"{pet.name}已经进入{self.name}")

    def check_all_pets(self):
        print(f"欢迎来到{self.name}，医生开始检查宠物：")

        for pet in self.pets:
            pet.eat()
            pet.sleep()
            pet.speak()
            print("检查完成")
            print("-" * 20)


hospital = PetHospital("阳光宠物医院")

cat = Cat("咪咪", 2)
dog = Dog("旺财", 3)
bird = Bird("小黄", 1)

hospital.add_pet(cat)
hospital.add_pet(dog)
hospital.add_pet(bird)

hospital.check_all_pets()


"""
咪咪已经进入阳光宠物医院
旺财已经进入阳光宠物医院
小黄已经进入阳光宠物医院
欢迎来到阳光宠物医院，医生开始检查宠物：
咪咪正在吃饭
咪咪正在睡觉
咪咪：喵喵喵
检查完成
--------------------
旺财正在吃饭
旺财正在睡觉
旺财：汪汪汪
检查完成
--------------------
小黄正在吃饭
小黄正在睡觉
小黄：叽叽叽
检查完成
--------------------


这段代码里面分别体现了什么？
1. 类
class Pet:
class Cat:
class Dog:
class Bird:
class PetHospital:

这些都是类。

类是对一类事物的抽象。

比如：

Pet 表示宠物
Cat 表示猫
Dog 表示狗
PetHospital 表示宠物医院
2. 对象
cat = Cat("咪咪", 2)
dog = Dog("旺财", 3)
bird = Bird("小黄", 1)
hospital = PetHospital("阳光宠物医院")

这些都是对象。

对象是类创建出来的具体实例。

3. 封装
self.name = name
self.age = age

把宠物的属性放到对象内部。

def eat(self):
def sleep(self):
def speak(self):

把宠物的行为也放到对象内部。

这就是封装。

4. 继承
class Cat(Pet):
class Dog(Pet):
class Bird(Pet):

猫、狗、鸟继承了宠物类。

它们不用重复写 name、age、eat()、sleep()，可以直接复用父类的代码。

这就是继承。

5. 多态
for pet in self.pets:
    pet.speak()

虽然代码都是：

pet.speak()

但是：

猫执行的是猫的 speak()
狗执行的是狗的 speak()
鸟执行的是鸟的 speak()

同一个方法，不同对象，不同表现。

这就是多态。


===========================================================================
你可以直接这样讲：

面向对象编程不是一开始就想着函数怎么写，而是先思考：我的程序里有哪些“事物”？
这些事物有什么属性？有什么行为？它们之间有什么关系？

拿宠物医院这个例子来说：

宠物是一类事物，所以定义 Pet
猫、狗、鸟都是宠物，所以它们继承 Pet
每只宠物都有名字和年龄，所以用属性保存
每只宠物都会吃饭、睡觉、叫，所以用方法表示行为
不同宠物叫法不一样，所以使用多态

最后一句总结：

类是模板，对象是实例；
封装是把数据和行为放一起；
继承是复用已有代码；
多态是同一个方法在不同对象上有不同表现。

"""