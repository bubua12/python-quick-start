"""
定义：类中所定义的方法，最终会保存在类身上，并且主要是通过实例调用，所以叫：实例方法。

特点：
1. 实例方法虽然最终会保存在类身上，但它主要是供实例使用的，所以才叫实例方法。
2. 因为收到了self参数，所以其内部可以：访问实例属性，调用实例方法。
3. 实例方法的主要作用：定义实例对象的具体行为。
"""


# 定义一个Person类
class Person:
    # 初始化方法（给实例添加属性）
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 下面的speak方法、run方法，都保存在类身上，但他们主要是供实例调用，所以他们都叫：实例方法
    # 自定义方法（给实例添加行为）
    def speak(self, msg):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我想说：{msg}')

    # 自定义方法（给实例添加行为）
    def run(self, distance):
        print(f'{self.name}疯狂的奔跑了{distance}米')


# 创建Person类的实例对象
p1 = Person('张三', 18, '男')
p2 = Person('李四', 22, '女')

print(Person.__dict__)
print(p1.__dict__)
print(p2.__dict__)

# 通过实例调用实例方法
p1.speak('你好')
p1.run(300)

# 通过类去调用实例方法(能调用，但不推荐)
Person.run(p2, 100)
