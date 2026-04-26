import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [4, 2, 5, 6, 8]
plt.plot(x, y)
plt.show()


# 定义函数（使用**kwargs去接收：可变关键字参数，kwargs只是大家习惯这么写，当然也可以换成其他变量）
def test2(**kwargs):
    # 此处kwargs的值，是一种新的数据类型，叫：字典，我们下一章就去讲字典
    print(kwargs)

# 调用函数
test2(name='张三', gender='男', age=18, height=172)