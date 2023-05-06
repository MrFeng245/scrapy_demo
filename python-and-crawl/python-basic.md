python基础知识

## <span style="color: orange;">python规范</span>

- 函数必须写注释：文档注释格式`'''注释内容'''`
- 参数中的等号两边不要用空格
- 相邻函数用两个空行隔开
- 小写 \+ 下划线
    1.  函数名
    2.  模块名
    3.  实例名
- 驼峰法
    1.  类名

## <span style="color: orange;">tips</span>

```python
# 一行代码太长，使用\折行
if xx and xxx and \
    xxx and xxx
```

```python
# 获取对象内存
import sys
sys.getsizeof(f)
```

# <span style="color: cornflowerblue;">变量和数据类型</span>

## <span style="color: orange;">字符串</span>

> 结构化类型，有一系列的属性和类型

### <span style="color: burlywood;">库函数</span>

```python
# 不会影响原来的变量，需要改变则需用变量接受返回值
string.title() # 首字母大写，其余小写
string.upper() # 全大写
string.lower() # 全小写
string.rstrip() # 仅删除末尾空格
string = string.rstrip()
string.lstrip() # 仅删除开头空格
string.strip() # 删除首尾空格，中间的不删
string.split(' ', num) # 以空格为分隔符，分隔num+1个，默认分隔所有 
```

### <span style="color: burlywood;">相关语法</span>

```python
# 字符串拼接
string = str1 + "hello"
```

```python
# r-string 非转义
print(r'\t') # output:\t
```

### <span style="color: burlywood;">格式化</span>

```python
# % 格式化
'i am %s, and he is %s' % (my_name, his_name)
```

```python
# format + 占位符 格式化
'i am {0}, and he is {1}'.format(my_name, his_name)
# 抑或
'i am {my_name}, and he is {his_name}'.format(my_name='li', his_name='wang')
# 也可混用
'i am {}, and he is{his_name}, we like to {}'.format(my_name, work, his_name='li')
```

```python
# f-string
f'i am {my_name}, and he is {his_name}'
```

## <span style="color: orange;">数字</span>

> 标量类型，此对象无可访问的内部对象

```python
# +-*/ <-> 加减乘除
# ** <-> 乘方
```

`python`中，整型相除默认是浮点型

# <span style="color: cornflowerblue;">基础语法</span>

## <span style="color: orange;">if 语句</span>

```python
# 检查特定值
arr = ['a', 'b', 'c']
if 'dd' not in arr:
    print('no')
```

```python
# if - elif - else
age = 40
if age < 12:
    print("you are baby")
elif age < 18:
    print("you are young")
else:
    print("you are adult")
```

建议：使用elif代替else

## <span style="color: orange;">循环结构</span>

### <span style="color: burlywood;">for - in</span>

- `range(101)`：可以用来产生0到100范围的整数，需要注意的是取不到101。
- `range(1, 101)`：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
- `range(1, 101, 2)`：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
- `range(100, 0, -2)`：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。

### <span style="color: burlywood;">while</span>

```python
num = 1;
while num <= 5:
    print(num)
    num += 1
```

```python
# 字符串while交互
prompt = '\nTell me someting, and I will repeat it back to you:'
prompt += "\nEnter 'quit' to end the program:"

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
```

## <span style="color: orange;">input - 输入</span>

```python
# input返回的结果是输入的内容，括号里的参数是字符串，可以显示在终端
age = input("请输入年龄：")
age = int(age)
print("你的年龄是：" + str(age))
```

## <span style="color: orange;">print - 输出</span>

```python
# 占位符格式 % 
a, b = 3, 4
print('a=%d, b=%d' % (a, b)) 
print('a=%d' % a) # 如果是一个参数，不需要括号
```

```python
# 格式化输出
# %f 浮点，%s 字符串
print('%.1f华氏度 = %.1f摄氏度' % (a, b))
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度') # 字符串前加f表示格式化字符串

# 输出字符串/数字
a, b = '5', '10'
print('{0} + {1} = {2}'.format(a, b, a+b))
print(f'{a} * {b} = {a * b}')
```

## <span style="color: orange;">函数</span>

> 函数名加括号就行执行，函数名不加括号就能传递

### <span style="color: burlywood;">定义</span>

```python
# 如果不想在本文件导出时，执行本函数，则写成下面的形式
def main():
    # Todo: Add your code here
    pass

if __name__ == '__main__':
    main()
# 如果代码在本文件中执行，则__name__的值为'__main__',否则为文件名
```

### <span style="color: burlywood;">传递实参</span>

```python
# 位置实参：实参与形参位置需要对应

# 关键字实参
def func(par1, par2):
    print(par1 + ' ' + par2)
func(par2 = 'name', par1 = 'my')

# 指定默认值
def func(par1, par2 = 'look'):
    print(par1 + ' ' + par2)
func(par1 = 'let me') # 也可func('let me') 【仅限末尾的形参已有默认值】
```

```python
# 切片可以创建列表副本
def function(cats[:]): # 则函数不会修改原来的cats列表
```

```python
# 传递任意数量实参 - cat 变为元组，无论是一个参数，两个参数还是没有参数
def function(*cat):
    print(cat)
function('a', 'aa', 'b')
```

```python
# 创建一个传任意参数的字典
def build_profile(**info):
    profile = {}
    for key, val in info.items():
        profile[key] = val
    print(profile)
build_profile(name = 'liming', age = 24, edu = '兰大')
```

### <span style="color: burlywood;">导入模块</span>

```python
# 导入module.py
import module
# 调用module中func函数
mode.func()

# 仅调入某函数
from module_name import function_name1, function_name2
```

```python
# as 给函数指定别名
from module import old_name as new_name
# as 起模块起别名
import module as m
```

```python
# 导入模块所有函数【不建议使用】
from module import *	# 此时调用函数时无需使用句号表示法
```

**<span style="color: red;">python同名函数或变量会进行覆盖</span>**

## <span style="color: orange;">异常</span>

### <span style="color: burlywood;">异常 - Error</span>

```python
try:
    # 代码块
except errorType:
    # 出现异常执行代码块
else:
    # 未出现异常执行代码块
finally:
    # 不论怎样都会执行代码块
```

```python
# 统计文件字数
def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = filename + " can't found"
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.") 

filenames = ['guest.txt', 'a.txt', 'b.txt']
for filename in filenames:
    count_words(filename)
```

```python
# 遇到异常时，不反馈
except errorType:
    pass
```

# <span style="color: cornflowerblue;">数据类型</span>

> 存储成组的信息，类似于数组，但可以容纳不同的类型的元素

## <span style="color: orange;">列表</span>

### <span style="color: burlywood;">初始化</span>

```python
# 声明与初始化
bicyles = ['trek', 'annondale', 'redline']
print(bicyles)	# 访问所有元素
print(bicyles[0])	# 访问单个元素
```

### <span style="color: burlywood;">索引对应关系</span>

```python
list1 = [1, 2, 3, 4]
# index	 0  1  2  3
# index	-4 -3 -2 -1
```

### <span style="color: burlywood;">增删</span>

```python
# 在列表中添加元素
list2 = [1, 2, 3, 4]
list2.append(5)	# 末尾
List2.insert(0, 10) # 索引+数值，插入元素

# 删除元素 
del list2[1] # 按索引删除
list2.pop()	# 默认从末尾删，也可在括号内指定索引，返回值是删除的元素
list2.remove(3) # 按值删除（只会删除第一次出现的值），返回值是空
del list1 # free list1
list1.clear() # 清空list1中元素
```

<span style="color: red;">关于remove</span>

- 如果remove的元素不在list中，可编译
- remove的元素类型与list中的元素类型不匹配时，会报错

<span style="color: red;">关于insert</span>

- 不会因为索引超出范围而报错，超出范围：正数-末尾；负数-开头
- `index = -1`，则会插入到倒数第二个位置，-2同理

### <span style="color: burlywood;">排序</span>

```python
# 永久性排序
list1.sort()	# 升序
list1.sort(reverse = True)	# 降序（注：python中的True，T要大写）

# 临时性排序
print(sorted(list1))	# 只能按sorted中的列表顺序正序排列
```

list中有不同类型的元素，排序会报错

### <span style="color: burlywood;">求表长</span>

```python
length1 = len(list1)
```

### <span style="color: burlywood;">逆置</span>

```python
list1.reverse() 	# 永久性的
```

### <span style="color: burlywood;">其余注意事项</span>

- 列表为空时，`index = -1` 会出错

## <span style="color: orange;">操作列表</span>

### <span style="color: burlywood;">遍历列表</span>

```python
for cat in cats:
    print(cat)
    
for i in range(len(cats)):
    print(cats[i])
    
for i, item in enumerate(cats):
    print(i, item)
```

### <span style="color: burlywood;">数值列表</span>

```python
# range(a, b) [a, b) 默认从0开始
for item in range(1, 5):
    print(item)

# range 指定步长
range(a, b, 2) # [a, b) 步长为2
```

```python
# range创建列表
numbers = list(range(1, 6))
print(numbers)
```

```python
# 统计数字列表
max(digits)
min(digits)
sum(digits)
```

```python
# 1~10 的平方列表
numbers = [number ** 2 for number in range(1, 11)]
print(numbers)
```

### <span style="color: burlywood;">切片</span>

```python
# 切片 [ , )
words = ['a', 'b', 'c', 'd']
print(words[0 : 3])	# ['a', 'b', 'c']

# 从第3个元素开始
print(words[2 : ])
# 输出前两个
print(words[ : 2])
# 输出最后三个
print(words[-3 : ])
# 中间三个
index = int(len(words) / 2)
print(words[index - 1:1 - index])

# 复制列表（赋值引用 words和newWords指向同一地址
newWords = words
# 复制列表（赋值数值 words和newWords再无关联
newWords = words[:]

# 逆序输出
newWords = words[::-1]
```

### <span style="color: burlywood;">生成式和生成器</span>

```python
# 生成器
f = (x ** 2 for x in range(1, 1000)) # x是局部变量，作用域仅在()中
for val in f:
    print(val)

# 生成式 生成列表
list_f = [x ** 2 for x in range(1, 1000)]
```

```python
# 相比于生成式需要的空间更少
print(sys.sizeof(f)) # 120
print(sys.sizeof(list_f)) # 9024
```

```python
# 生成器：内存更小，响应更快
def square(n):
    for i in range(n):
        yield i ** 2
        
for item in square(5):
    print(item)
    
# 普通写法
def square(n):
    arr = [x ** 2 for x in range(n)]
    return arr

for item in square(5):
    print(item)
```

### <span style="color: burlywood;">元组 \- 不可变的列表</span>

> 不可变的列表称为元组
>
> 在多线程环境中，相较于列表更加安全，更加高效

```python
# 定义元组
dimensions = (1, 2, 3)
print(dimensions[0])
# tup1 = (50,) 仅包含一个元素时，需要在后面加逗号
```

```python
# 覆盖原有元组
dimensions = (1, 2, 4)
dimensions = (1, 2, 3)
print(dimensions)
```

```python
# 元组转化为列表
list1 = list(dimensions)
```

## <span style="color: orange;">集合</span>

> 不允许有重复元素，可进行集合的交并差运算

```python
# 创建集合的字面量语法 空集合必须用set创建
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length =', len(set1))
# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)
```

```python
print('\n')
set1.add(4)
set2.update([11, 12]) # 添加元素
set2.discard(5) # 删除元素
if 4 in set2:
    set2.remove(4)
print(set1, set2)
print(set3.pop())
print(set3)
```

## <span style="color: orange;">字典</span>

> 一系列键值对

### <span style="color: burlywood;">初始化</span>

```python
# 声明+初始化
alien = {'color': 'green', 'points': 5}
# 访问
print(alien['color'])
```

### <span style="color: burlywood;">增删改查</span>

```python
# 增
alien['x_pos'] = 0
alien['y_pos'] = 20
# 改
alien['x_pos'] = 40
# 删
del alien['color']
```

```python
# 查键值(第一个元素是键，第二个元素是值；key和value只是变量名)
for key, value in alien.items():	# items()访问各个键值对
    print("\nKey:" + key + "\tValue:" + str(value))
# 查键、值
for key in alien.keys():
    print(key)
for value in alien.values():
    print(str(value))
    
# keys() - 返回包含字典中所有键的列表
print(alien.keys())
# values() - 返回包含字典中所有值的列表
print(alien.values())

# 查值 【查键同理】
for value in alien.values():		# 默认第一个是值 - for value in alien:
    print(str(value))
```

```python
# set过滤重复
for value in set(alien):
# sorted() - 按序遍历（默认顺序随缘）
for key in sorted(alien.keys()):
    print(key.title())
```

## <span style="color: orange;">各类操作小结</span>

> 列表、元组、集合、字典的操作

```python
# 打印函数 用于测试
def print_list():
    print('list1: ' + str(list1))
    print('set1: ' + str(set1))
    print('tup1: ' + str(tup1))
    print('dict1: ' + str(dict1))
```

### <span style="color: burlywood;">创建</span>

```python
# 字面量语法
list1 = [1,2,3,4]
set1 = {1,2,3,4}
tup1 = (1,2,3,4)
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

### <span style="color: burlywood;">添加元素</span>

```python
def add_item(n):
    list1.append(n)
    set1.add(n)
    # tup1 元组不可增加元素
    dict1['e'] = 5
```

### <span style="color: burlywood;">删除元素</span>

```python
# 清空元素
def clear_item():
    list1.clear()
    set1.clear()
    # tup1 元组不能清空元素
    dict1.clear()
```

```python
# 弹出元素
def pop_item():
    list1.pop() # 列表弹出最后一个加入的
    set1.pop() # 集合弹出第一个加入的
    # tup1 元组不能弹出元素
    # dict1 字典不能弹出元素
```

```python
# 删除元素
def del_item():
    del list1[0] # 按值删
    list1.remove(4) # 按索引删
    set1.discard(1) # 按值删
    # tup1 元组不能删除元素
    del dict1['a']
```

### <span style="color: burlywood;">查找元素</span>

```python
# 查找
def find1_item(index):
    print(list1[index])
    # set1 集合无序不重复，无法通过索引查找
    print(tup1[index])
    print(dict1['a']) # 键查值
    print(dict1.keys()) # 查键列表
    print(dict1.values()) # 查值列表
```

```python
# 遍历
def for_item():
    for l, s, t, d in list1, set1, tup1, dict1:
        print(l)
        print(s)
        print(t)
        print(d)
```

```python
# 查询
def find2_item(n):
    if n in list1:
        print('yes')
    if n in set1:
        print('yes')
    if n in tup1:
        print('yes')
    if n in dict1:
        print('yes')
```

## <span style="color: orange;">嵌套</span>

### <span style="color: burlywood;">字典列表</span>

```python
# 字典列表 <=> 对象集合
aliens = []
for alien_number in range(4):
    alien = {'color': 'green',
             'number': alien_number,
             'points': 5,
             'speed': 'slow'
            }
    aliens.append(alien)
for alien in aliens:
    print(alien)
```

### <span style="color: burlywood;">列表字典</span>

```python
# 列表字典 <=> 更丰富的字典/对象
cat = {
    'color': 'black',
    'name': ['小黑', 'tom']
}
print(cat)
```

### <span style="color: burlywood;">字典的字典</span>

```python
# 字典的字典 <=> 更丰富的字典/对象
user = {
    'liMing': {
       'email': '123@qq.com', 
        'state': 'common',
    },
    'wangHu': {
        'email': '66993@qq.com', 
        'state': 'member',
    },
}
print(user)
```

## <span style="color: orange;">类</span>

> 类方法：
>
> - 公有
> - 私有 类名以两个下划线开头（子类无法访问父类的私有属性）

### <span style="color: burlywood;">创建类</span>

```python
# 创建类
class cat():
    '''模拟猫'''
    # self形参必须定义在第一位，系统传实参，调用时仅传后两个参数即可
    def __init__(self, name):	# 初始化函数名是固定的
        '''初始化属性name和age'''
        self.name = name	# self用句号表示法访问变量/属性
        self.age = 4
        
    def sit(self):
        '''模拟猫坐下'''
        print(self.name.title() + " is now sitting")
        
    def roll_over(self):
        '''模拟猫打滚'''
        print(self.name.title() + " is now rolling")
        
    def read_age(self):
        print(self.name.title() + " is " + str(self.age) + " year age.")
```

```python
# 创建实例
my_cat = cat('花花', 3)
print("My cat's name is " + my_cat.name.title() + '.')
print("My cat is " + str(my_cat.age) + " years age.")
```

```python
# 修改属性
my_cat.age = 80 # 直接访问
my_cat.read_age()

# 创建方法
def update_age(self, age):
    self.age = age
my_cat.update_age(40)
```

### <span style="color: burlywood;">继承</span>

> 要求：父类包含在当前文件中，且位于子类前

```python
# 类继承
class Restaurant():
    '''餐厅类'''
    def __init__(self, restaurant_name, restaurant_type):
        '''初始化属性name和type'''
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.number = 0
        
    def open_restaurant(self):
        '''打印开店'''
        print(self.restaurant_name + " is opening")
        
class Chinese_restaurant(Restaurant):	# 注意此处要传入父类
    '''中式餐厅'''
    def __init__(self, restaurant_name, restaurant_type):
        '''初始化父类的属性'''
        super().__init__(restaurant_name, restaurant_type)	# super()辅助继承
        self.level = 3	# 增加子类属性
    
    def open_restaurant(self):
        '''重写开店'''
        print(self.restaurant_name + " will open in 8:00.")
        
my_chinese_restaurant = Chinese_restaurant('好运来', '川菜')
my_chinese_restaurant.open_restaurant()
```

```python
# 类嵌套
'''定义一个类class1，在另一个类中定义一个属性，其右值是之前定义的类：class1()'''

# 从模块中导入类
from module import Restaurant
```

```python
# 类库 - 有序字典
from collections import OrderdDict
people = OrderdDict()
people['name'] = 'liMing'
people['age'] = 26
```

### <span style="color: burlywood;">闭包</span>

> 闭包：定义一个函数中的函数，同时这个函数引用外层函数的变量
>
> 装饰器：为已存在的对象添加额外的功能，有助于让代码更简短

场景：需要为多个函数`x()`增加一个功能时，可以把此功能定义出来`func()`，并在参数中增加一个函数，此时的需求可以实现，但是调用时：`func(x)`，此种调用方式破坏了原有的函数结构。故而使用装饰器为原有函数增加功能。

- <span style="color: red;">装饰器</span>

```python
# 简单的装饰器
def use_logging(func):

    def wrapper():
        logging.warn("%s is running" % func.__name__)
        return func()   # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
    return wrapper

def foo():
    print('i am foo')

foo = use_logging(foo)  # 因为装饰器 use_logging(foo) 返回的时函数对象 wrapper，这条语句相当于  foo = wrapper
foo()                   # 执行foo()就相当于执行 wrapper()
```

```python
# 语法糖
def use_logging(func):

    def wrapper():
        logging.warn("%s is running" % func.__name__)
        return func()
    return wrapper

@use_logging # 代替 foo = use_logging(foo) 语句
def foo():
    print("i am foo")

foo()
```

```python
# 指定参数
def wrapper(name):
        logging.warn("%s is running" % func.__name__)
        return func(name)
    return wrapper
```

```python
# 类装饰器顺序
@a
@b
@c
def f ():
    pass
```

- <span style="color: red;">访问器和修改器</span>

python用一个下划线说明属性不建议修改（实际可以修改通过访问器和修改器操作）：

```python
class Person(object):
    
    # __slots__ 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute
    person._gender = '男'
    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True


if __name__ == '__main__':
    main()
```

### <span style="color: burlywood;">静态方法和类方法</span>

```python
# 静态方法：调用类方法使无需创建对象
from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # 声明类的静态方法
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))


def main():
    a, b, c = 3, 4, 5
    # 静态方法直接调用（静态方法和类方法都是通过给类发消息来调用的）
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 给类传入对象：通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t))
        print(t.area())
        # print(Triangle.area(t))
    else:
        print('无法构成三角形.')


if __name__ == '__main__':
    main()
```

```python
# 创建类方法对象
from time import time, localtime, sleep


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second
        
    # cls是约定名
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
```

### <span style="color: burlywood;">继承的三种关系</span>

- `is - a`：继承或泛化
- `has - a`：关联。整体和部分的关系
- `use - a`：依赖。一个类方法的参数用到了另一个类

### <span style="color: burlywood;">多态</span>

> 多态：同样的方法，由于传入不同的对象，因而产生不同的状态

```python
from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
```

# <span style="color: cornflowerblue;">测试代码</span>

## <span style="color: orange;">测试函数</span>

```python
# func.py
def get_formatted_words(first, last):
    '''generate a neatly formatted full name.'''
    full_words = first + ' ' + last
    return full_words
```

```python
# test.py
import unittest
from func import get_formatted_words

# 继承自类 unittest.TestCase()
class WordsTestCase(unittest.TestCase):
    '''测试get_formatted_name'''
    # 定义一个测试函数【再定义测试函数时，需要不同的函数名】
    def test_words(self):
        '''能正确处理 look up 这样的短语吗'''
        formatted_words = get_formatted_words('look', 'up')
        self.assertEqual(formatted_words, 'look up') # 判相等
        
unittest.main()
```

## <span style="color: orange;">测试类</span>

| 方法                      | 用途                   |
| ------------------------- | ---------------------- |
| `assertEqual(a, b)`       | 核实`a == b`           |
| `assertNotEqual(a, b)`    | 核实`a != b`           |
| `assertTrue(x)`           | 核实`x == True`        |
| `assertFalse(x)`          | 核实`x == False`       |
| `assertIn(item, list)`    | 核实`item in list`     |
| `assertNotIn(item, list)` | 核实`item not in list` |

### <span style="color: burlywood;">测试一组类对象</span>

```python
# func.py
class AnonymousSurvey():
    '''收集匿名调查问卷的答案'''
    
    def __init__(self, question):
        '''存储一个问题，并为存储答案做准备'''
        self.question = question
        self.answers = []
        
    def show_question(self):
        '''显示问卷问题'''
        print(question)
        
    def store_response(self, new_response):
        '''存储单份问卷答案'''
        self.answers.append(new_response)
        
    def show_results(self):
        '''显示收集到的所有答案'''
        print('suvery result:')
        for answer in answers:
            print('- ' + answer)
```

```python
# test.py
import unittest
from test import AnonymousSurvey

class SuveryTestCase(unittest.TestCase):
    '''测试get_formatted_name'''
    
    def test_store(self):
        '''能正确处理存储答案吗'''
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['Chinses', 'Japanses', 'English']
        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, my_survey.answers)
        
unittest.main()
```

### <span style="color: burlywood;">setUp() - 创建对象一次</span>

```python
# test.py 所有数据都要通过self调用
import unittest
from test import AnonymousSurvey

class SuveryTestCase(unittest.TestCase):
    '''测试get_formatted_name'''
    
    def setUp(self):
        '''能正确处理存储答案吗'''
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Chinses', 'Japanses', 'English']
        
    def test_store(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.answers)
        
unittest.main()
```

终端输出与结果的对应关系：

| 显示 | 测试结果 |
| ---- | -------- |
| `.`  | 通过     |
| `E`  | 错误     |
| `F`  | 断言失败 |

# <span style="color: cornflowerblue;">文件</span>

## <span style="color: orange;">操作模式</span>

| 操作模式 | 具体含义                         |
| -------- | -------------------------------- |
| `'r'`    | 读取 （默认）                    |
| `'w'`    | 写入（会先截断之前的内容）       |
| `'x'`    | 写入，如果文件已经存在会产生异常 |
| `'a'`    | 追加，将内容写入到已有文件的末尾 |
| `'b'`    | 二进制模式                       |
| `'t'`    | 文本模式（默认）                 |
| `'+'`    | 更新（既可以读又可以写）         |

### <span style="color: burlywood;">读 \- read</span>

```python
 # 读文本文件【同目录下文件】
 # open(路径+文件名) 返回一个文件对象，存储在变量file_object中
 file_path = 'file_name'
 # 默认是读，可也指定 open(file_path, 'r', encoding='utf-8')
 with open(file_path) as file_object:    # with 让程序在合适的时机关闭文件
     contents = file_object.read()   # read 在文件末尾是返回一个空字符串，即相比与原文件多出一个空行
     print(contents)
 # 删除空行的方法 contents.rstrip()
 
 # 读二进制文件
 with open(file_path, 'rb') as f_obj:
     date = f_obj.read()
     print(type(date))
 # 相对路径 基于程序所在的文件夹
 file_path = 'txt\file_name'
 
 # 绝对路径
 file_path = 'C:\Users\MrFeng\Documents\python\txt\pi.txt'
```

问题：\\U \\M 会被理解为未编码的转义字符，报错

解决方法：

- `\`替换为`/`【Linux系统和OS X系统写法】
- 加`r`显式声明不使用转义字符`func(r"xxx")`
- 使用`\`的转义字符`\\`

```python
 # 每次一行读取 for
 with open(file_path) as file_object:
     for line in file_object:
         print(line.rstrip() + '.')
         
 # 另一种方式 readlines
 with open(file_path) as file_object:
     lines = file_object.readlines()
 for line in lines:
     print(lint.rstrip() + '.')
```

### <span style="color: burlywood;">写 \- write</span>

```python
 # 向文件写入内容
 file_path = r'pi.txt' # 不加转义
 with open(file_path, 'w') as file_object:
     file_object.write("I love Programming\n")
     
 # 追加文件
 open(file_path, 'a')
```

注意事项：

- 若不存在此文件，会创建
- 若原来文件中有内容，会被覆盖

write 和 writelines 区别

- write(字符串)
- writelines(序列)

## <span style="color: orange;">文件类型</span>

### <span style="color: burlywood;">JSON文件</span>

> javascript object notation 一种存储格式，字典格式（可用编译器打开）
>
> 序列化：将数据结构或对象转化成可存储的形式

json模块主要有四个比较重要的函数，分别是：

- `dump` \- 将Python对象按照JSON格式序列化到**文件**中
- `dumps` \- 将Python对象处理成JSON格式的**字符串**
- `load` \- 将**文件**中的JSON数据反序列化成对象
- `loads` \- 将**字符串**的内容反序列化成Python对象

```python
 import json
 numbers = [200, 3, 4, 6, 7, 8]
 
 filename = 'numbers.json'
 # dump(data, file) data写入file
 with open(filename, 'w') as f_obj:
     json.dump(numbers, f_obj)
 # load(file) file 写入内存
 with open(filename) as f_obj:
     nums = json.load(f_obj)
 print(nums)
 # 把名字写入json文件，下次运行时打开此json文件，读取名字
 import json
 
 filename = 'username.json'
 def input_info():
     msg = "输入你的名字，sir："
     username = input(msg)
     with open(filename, 'w', encoding='utf-8') as f_obj:
         json.dump(username, f_obj)
 
 def open_file():
     with open(filename) as f_obj:
         username = json.load(f_obj)
     return username
     
 def judge_user(username):
     msg = username + " is your name(y/n):"
     judge = input(msg)
     if judge == 'y':
         print("欢迎回来，" + username + ".")
     else:
         input_info()
         
 def greet_user():
     try:
         username = open_file()
     except FileNotFoundError:
         input_info()
     else:
         judge_user(username)
 
 greet_user()
```

### <span style="color: burlywood;">text文件</span>

> 记事本打开

```python
def save_file():
    '''把数据保存为json文件和格式化的text文件'''    
    txt_filename = '酷狗Top500歌单信息.txt'
    
    for data in datas:
        msg = f"第{data['rank']}名，歌名《{data['song']}》，由{data['singer']}演唱，时长：{data['time']}\n"
        with open(txt_filename, 'a', encoding='utf-8') as f:
            f.write(msg)
    print('写入成功')
```

### <span style="color: burlywood;">csv文件</span>

> EXCEL打开，之间用逗号分隔
