<h1 align="center"> Python Quick Start</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14.x-green" alt="Python">
  <img src="https://img.shields.io/badge/IDE-PyCharm-21D789" alt="PyCharm">
  <img src="https://img.shields.io/badge/Topic-Python%20Basics-blue" alt="Python Basics">
  <img src="https://img.shields.io/badge/Topic-OOP-orange" alt="OOP">
  <img src="https://img.shields.io/badge/Status-Learning%20Project-brightgreen" alt="Status">
</p>

<p align="center">
  一个面向 Python 初学者的快速入门练习项目，覆盖基础语法、运算符、数据结构、异常处理与面向对象编程。
</p>

---

## 项目简介

`python-quick-start` 是一个按知识点拆分的 Python 学习仓库。每个 `.py` 文件都围绕一个主题编写小案例，方便按顺序阅读、运行和练习。

项目内容从变量与数据类型开始，逐步过渡到函数、集合类型、异常处理，再到类、对象、属性、方法、继承、封装和多态等面向对象核心概念。

## 技术栈

| 技术 | 说明 |
| --- | --- |
| Python 3.14.x | 主要编程语言 |
| PyCharm | 推荐开发环境 |
| Git | 版本管理工具 |

## 目录结构

```text
python-quick-start/
├── 01_base.py                         # 数据类型与类型转换
├── 02_opeartor.py                     # Python 运算符示例
├── 03_flow.py                         # 流程控制语句
├── 04_function.py                     # 函数基础
├── 05_datastruct.py                   # 列表、元组、集合、字典
├── 06_exception.py                    # 异常处理
├── 07_oop.py                          # 类与对象基础
├── oop_demo01/
│   ├── animal.py                      # 宠物医院 OOP 案例
│   └── oop_demo1.py                   # 面向对象演示入口
├── oop_demo02/
│   └── drink.py                       # 奶茶店点单 OOP 案例
└── oop_primary/
    ├── 01_property/
    │   ├── 01_obj_property.py         # 实例属性
    │   └── 02_class_property.py       # 类属性
    └── 02_method/
        ├── 01_obj_method.py           # 实例方法
        ├── 02_class_obj.py            # 类方法
        └── 03_static_method.py        # 静态方法
```

## 学习内容

### Python 基础

- 变量声明
- 常见数据类型
- 类型转换
- 算术、比较、赋值、逻辑运算符
- 函数定义与调用

### 常用数据结构

- `list`：列表的增删改查
- `tuple`：不可变有序序列
- `set`：去重与成员判断
- `dict`：键值对存储与访问

### 异常处理

- `try-except`
- 多异常捕获
- `else`
- `finally`
- 自定义异常类

### 面向对象编程

- 类与对象
- 实例属性与类属性
- 实例方法、类方法、静态方法
- 封装
- 继承
- 多态
- 综合案例：宠物医院、奶茶店点单系统

## 环境要求

- Python 3.14.x
- PyCharm 或其他 Python IDE
- Git

## 快速开始

### 1. 克隆项目

```bash
git clone <your-repository-url>
cd python-quick-start
```

### 2. 创建虚拟环境

```bash
python -m venv .venv
```

### 3. 激活虚拟环境

Windows：

```bash
.venv\Scripts\activate
```

macOS / Linux：

```bash
source .venv/bin/activate
```

### 4. 运行示例

```bash
python 01_base.py
python 05_datastruct.py
python 06_exception.py
python oop_demo02/drink.py
```

## 推荐学习顺序

1. `01_base.py`：认识变量、数据类型和类型转换
2. `02_opeartor.py`：理解常用运算符
3. `03_flow.py`：学习流程控制语句
4. `04_function.py`：掌握函数定义
5. `05_datastruct.py`：练习常用数据结构
6. `06_exception.py`：学习异常处理
7. `07_oop.py`：理解类与对象
8. `oop_primary/`：深入实例属性、类属性和方法类型
9. `oop_demo01/`、`oop_demo02/`：通过完整案例理解面向对象思想

## 示例运行

运行奶茶店点单案例：

```bash
python oop_demo02/drink.py
```

你会看到类似输出：

```text
加入茶底、牛奶和珍珠，制作一杯大杯的珍珠奶茶，糖度：少糖
加入茶底和新鲜柠檬，制作一杯中杯的柠檬果茶，糖度：半糖
加入茶底、牛奶和椰果，制作一杯小杯的椰果奶茶，糖度：全糖
```

## 适合人群

- Python 零基础学习者
- 正在复习 Python 基础语法的开发者
- 想通过小案例理解面向对象编程的人

## 后续可扩展方向

- 补充流程控制示例：`if`、`for`、`while`
- 增加文件读写案例
- 增加模块与包的使用示例
- 增加简单命令行小项目
- 增加单元测试示例

## License

本项目用于 Python 学习与练习，可根据需要自由修改和扩展。
