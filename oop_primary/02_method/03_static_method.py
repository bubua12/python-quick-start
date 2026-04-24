"""
定义：使用@staticmethod装饰器修饰，方法没有self或cls参数，只是单纯的定义在类中。

特点：
1. 可通过『类名』或『实例名』调用，但强烈推荐通过类名调用以体现语义。
2. 由于没有self或cls参数，所以静态方法中通常：不访问类属性，也不访问实例属性。
3. 一般用于：定义与类相关，但可以独立使用的工具方法。

"""


# 定义一个Person类
class Person:
    # *******************************
    # *******************************
    # *******************************

    # 静态方法
    # 使用 @staticmethod 装饰过的方法，就叫：静态方法，静态方法也是保存在类身上的
    # 静态方法只是单纯的定义在类中，它不会收到：self、cls参数，它收到的参数都是自定义参数
    # 由于静态方法没有收到：self、cls参数，所以其内部不会访问任何：类和实例相关的内容
    # 静态方法通常用于定义：与类相关的工具方法
    @staticmethod
    def is_adult(year):
        # 获取当前的年份
        current_year = datetime.now().year
        # 计算年龄
        age = current_year - year
        # 返回结果（成年True，未成年False）
        return age >= 18

    @staticmethod
    def mask_idcard(idcard):
        return idcard[:6] + '********' + idcard[-4:]


# 验证一下：静态方法也是保存在类身上的
# print(Person.__dict__)

# 静态方法需要通过类去调用
# result = Person.is_adult(2015)
# print(result)
# result2 = Person.mask_idcard('212101198802030028')
# print(result2)

# 注意点：通过实例也能调用到静态方法，但非常不推荐
p1 = Person('张三', 18, '男')
res = p1.mask_idcard('212101198802030028')
print(res)
