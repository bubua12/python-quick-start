# 奶茶店点单系统
"""
面向对象的思想就是：
不要一上来就想“程序要一步一步怎么跑”，而是先想“这个世界里有哪些对象，它们有什么属性，能做什么事”。

比如奶茶店里有：
饮品
奶茶
果茶
订单
顾客
店员
在程序里，我们可以把“饮品”抽象成一个类。

类：像一张设计图，比如“饮品模板”。
对象：根据这张设计图做出来的具体东西，比如“一杯大杯少糖珍珠奶茶”。

"""


class Drink:
    """饮品类：所有饮品共有的模板"""

    # 这里有三个属性，分辨类里面的属性，还是参数，要看self后面的，self跟着的就是对象的属性
    def __init__(self, name, size, sugar):
        self.name = name
        self.size = size
        self.__sugar = sugar  # 私有属性，不希望外部随便改。外部不能通过对象.的形式来调用（修改或获取）
        # 私有属性，类里面的方法是可以访问的，如get_sugar

    # 获取糖度
    def get_sugar(self):
        return self.__sugar

    # 这里是“封装”特性的一个比较好的说明
    def set_sugar(self, sugar):
        if sugar not in ["无糖", "少糖", "半糖", "全糖"]:
            print("糖度不合法，默认改为半糖")
            self.__sugar = "半糖"
        else:
            self.__sugar = sugar

    def make(self):
        print(f"制作一杯{self.size}的{self.name}，糖度：{self.__sugar}")


class MilkTea(Drink):
    """奶茶类：继承自饮品"""

    def __init__(self, name, size, sugar, topping):
        # 这里相当于调用父类的构造方法 可以先忽略
        super().__init__(name, size, sugar)
        self.topping = topping

    # Overrides method in Drink
    def make(self):
        print(
            f"加入茶底、牛奶和{self.topping}，制作一杯{self.size}的{self.name}，糖度：{self.get_sugar()}"
        )


class FruitTea(Drink):
    """果茶类：继承自饮品"""

    def __init__(self, name, size, sugar, fruit):
        super().__init__(name, size, sugar)
        self.fruit = fruit

    def make(self):
        print(
            f"加入茶底和新鲜{self.fruit}，制作一杯{self.size}的{self.name}，糖度：{self.get_sugar()}"
        )


# 实例化对象：真正点出来的几杯饮品
drink1 = MilkTea("珍珠奶茶", "大杯", "半糖", "珍珠")

drink1.name="奥利奥"
# .sugar，是.不出来的，只能通过提供的方法来调用修改sugar，但是sugar是收到校验的，这里就是封装的好处
drink1.set_sugar("一百度糖")


drink2 = FruitTea("柠檬果茶", "中杯", "半糖", "柠檬")
drink3 = MilkTea("椰果奶茶", "小杯", "全糖", "椰果")

orders = [drink1, drink2, drink3]

for drink in orders:
    drink.make()

"""
一、封装
封装就是：把数据和操作数据的方法放在一起，并且控制外部怎么访问它。

在例子里：
self.__sugar = sugar
糖度被写成了私有属性，外部不能随便乱改。要改糖度，应该通过：set_sugar()，这样就能检查糖度是否合法。

封装就像奶茶店不会让顾客自己跑进后厨乱加糖，而是通过店员下单。程序也一样，不让外部随便改内部数据，而是提供安全的入口。

二、继承
继承就是：子类可以复用父类已有的属性和方法。

在例子里：
class MilkTea(Drink):
class FruitTea(Drink):
MilkTea 和 FruitTea 都是饮品，所以它们继承了 Drink

它们都有：
name
size
sugar

但它们又有自己的特色：
MilkTea 有 topping
FruitTea 有 fruit

继承就像“奶茶”和“果茶”都属于“饮品”。它们不用重新声明自己都有名字、杯型、糖度，因为这些通用特征已经在父类 Drink 里定义好了。

三、多态
多态就是：同一个方法名，在不同对象上有不同表现。

在例子里，三个对象都调用：
drink.make()

但是结果不同。

多态就像店员只需要说“开始制作”，但奶茶师知道奶茶该怎么做，果茶师知道果茶该怎么做。调用方式一样，执行效果不同。

类是模板，对象是具体东西；封装管内部，继承省重复，多态让同一个动作表现出不同效果。
"""
