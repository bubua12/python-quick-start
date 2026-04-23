# 案例演示：Python的异常处理


# 示例1：简单的try-except语句
try:
    # 尝试执行可能会抛出异常的代码
    result = 10 / 0
except ZeroDivisionError:
    # 当出现ZeroDivisionError异常时执行这里的代码
    print("Error：除数不能为零")

# 示例2：捕获多个异常
try:
    # 尝试将字符串转为整数
    num = int('abc')
except ValueError:
    # 当出现ValueError异常时执行这里的代码
    print("Error：无法将字符串转为整数")
except TypeError:
    # 当出现TypeError异常时执行这里的代码
    print("Error：类型错误")

# 示例3：使用else子句
try:
    # 尝试执行可能会抛出异常的代码
    result = 10 / 2
except ZeroDivisionError:
    # 当出现ZeroDivisionError异常时执行这里的代码
    print("Error：除数不能为零")
else:
    # 如果没有异常发生，则执行这里的代码
    print("结果是：", result)

# 示例4：使用finally子句
try:
    # 尝试打开一个不存在的文件
    file = open('file.txt', 'r')
except FileNotFoundError:
    # 当出现FileNotFoundError异常时执行这里的代码
    print("Error：文件未找到")
finally:
    # 无论是否发生异常，都会执行这里的代码
    print("已关闭对文件的操作")


# 示例5：自定义异常
class CustomException(Exception):
    # 自定义异常类，继承自Exception
    pass


try:
    # 抛出自定义异常
    raise CustomException("这是一个自定义异常")
except CustomException as e:
    # 当出现CustomException异常时执行这里的代码
    print("CustomException", e)
