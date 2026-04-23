# 案例演示python的所有数据类型

# 1、声明很多变量，并用到各种数据类型
# 整数
integer_variable = 36

# 浮点数
float_variable = 3.14

# 字符串
string_variable = "Hello, World"

# 布尔值
boolean_variable = True

# 列表
list_variable = [1, 2, 3, 4, 5]

# 元组
tuple_variable = (1, "two", 3)

# 集合
set_variable = {1, 2, 3, 4, 5}

# 字典 Map
dictionary_variable = {"name": 'Jone', "age": 23}

# 2、打印这些类型的变量
# print(f"整数变量类型: {type(integer_variable)}")
# print(f"浮点数变量类型: {type(float_variable)}")
# print(f"字符串变量类型: {type(string_variable)}")
# print(f"布尔值变量类型: {type(boolean_variable)}")

# 3、编写几个类型转换案例

# 整数转浮点数
int_to_float = float(integer_variable)
print(f"整数 {integer_variable} 转换为浮点数: {int_to_float}")

# 浮点数转整数（直接截断小数部分）
float_to_int = int(float_variable)
print(f"浮点数 {integer_variable} 转换为整数: {float_to_int}")

# 字符串转整数
string_to_int = int('123')
print(f"字符串 '123' 转换为整数: {string_to_int}")
# 注意：字符串转为整数，需要字符串本身就是数字类型的字符串

# 字符串转浮点数
string_to_float = float('3.1415926')
print(f"字符串 '3.1415926' 转换为浮点数: {string_to_float}")

# 列表转元组
list_to_tuple = tuple(list_variable)
print(f"列表 {list_variable} 转换为元组: {list_to_tuple}")

# 元组转列表
tuple_to_list = list(tuple_variable)
print(f"元组 {tuple_variable} 转换为列表: {tuple_to_list}")

# 列表转集合（自动去重）
list_to_set = set(list_variable)
print(f"列表 {list_variable} 转换为集合: {list_to_set}")

# 字典的键转列表
dict_keys_to_list = list(dictionary_variable.keys())
print(f"字典 {dictionary_variable} 的键转列表: {dict_keys_to_list}")

# 字典的值转列表
dict_values_to_list = list(dictionary_variable.values())
print(f"字典 {dictionary_variable} 的值转列表: {dict_values_to_list}")

# 布尔值转整数（True为1，False为0）
bool_to_int = int(boolean_variable)
print(f"布尔值 {boolean_variable} 转整数: {bool_to_int}")
