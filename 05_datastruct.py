# 案例演示: Python的数据结构
# 列表List、元组Tuple、集合Set、字典Dict

# 1、列表（List）
# 列表是一种可变的有序序列，可以包含不同类型的元素

# 创建列表
my_list = [1, 2, 3, 4, 5]

# 查：访问列表元素
print("列表中索引为2的元素：", my_list[2])

# 增：添加元素
my_list.append(6)  # 在列表末尾添加元素
print("添加元素后的列表：", my_list)

# 改：修改元素
my_list[2] = 10  # 将索引为2的元素修改为10
print("修改元素后的列表：", my_list)

# 删：删除元素
del my_list[2]  # 删除索引为2的元素
print("删除元素后的列表：", my_list)

# 2、元组（Tuple）
# 元组是一种不可变的有序序列，可以包含不同类型的元素

# 创建元组
my_tuple = (1, 2, 3, 4, 5)

# 查：访问元组元素
print("元组中索引为2的元素：", my_tuple[2])

# 元组是不可变的，因此不能进行增、改、删操作


# 3、集合（Set）
# 集合是一种无序且唯一的数据结构，用于存储不重复的元素

# 创建集合
my_set = {1, 2, 3, 4, 5}

# 查：检查元素是否存在
print("元素3是否存在集合中：", 3 in my_set)

# 增：添加元素
my_set.add(6)
print("添加元素后的集合：", my_set)

# 删：删除元素
my_set.remove(3)  # 删除元素 3
print("删除元素后的集合：", my_set)

# 4、字典（Dictionary）
# 字典是一种无序的键值对集合，键必须是唯一的

# 创建字典
my_dict = {"name": "Jack", "age": 23, "city": "New York"}

# 查：访问字典元素
print("字典中键 `name` 对应的值：", my_dict["name"])

# 增：添加键值对
my_dict['job'] = 'Coder'
print("添加键值对后的字典：", my_dict)

# 改：修改键值对
my_dict['city'] = "California"
print("修改键值对后的字典：", my_dict)

# 删：删除键值对
del my_dict['city']
print("删除键值对后的字典：", my_dict)
