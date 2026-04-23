# 定义一个类（类名通常用大驼峰写法）
class ClassName:
    # 当一个函数被定义在类中时，它就被称为“方法”。
    # __init__方法又叫：初始化方法，它主要用来给当前实例对象添加属性。
    # __init__方法收到的参数是：当前正在创建的实例对象、其他自定义参数。
    # 当我们后期编写代码，对类进行实例化的时候，Python就会自动调用__init__方法，去完成对实例的初始化。
    def __init__(self, param1, param2, param3):
        # 通过self给当前实例添加属性，语法格式为：self.属性名 = 属性值
        self.property = param1
        self.property = param2
        self.property = param3