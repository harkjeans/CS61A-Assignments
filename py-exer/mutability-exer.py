## 不可变数据类型

# 整数 (int)
a = 10
print(f"初始a: {a}, id: {id(a)}") # 初始a: 10, id: 140720343266504
a = a + 1  # 这不是修改10，而是创建了一个新的整数11
print(f"修改后a: {a}, id: {id(a)}") # 修改后a: 11, id: 140720343266536

# 字符串 (str)
s = "hello"
print(f"初始s: {s}, id: {id(s)}") # 初始s: hello, id: 2369836235632
s = s + " world" # 创建了一个新的字符串
print(f"修改后s: {s}, id: {id(s)}") # 修改后s: hello world, id: 2369836400432

# 元组 (tuple) - 容器本身不可变，但其内部的可变元素是隐患
t = (1, 2, [3, 4])
# t[0] = 5  # 这会报错：TypeError，因为元组元素不能被重新赋值
print(f"元组t: {t}, id: {id(t)}") # 元组t: (1, 2, [3, 4]), id: 2531938380352
t[2].append(5) # 但是元组内部的列表是可变的！可以修改它。
print(f"修改内部列表后t: {t}, id: {id(t)}") # 元组t的id没变！但它的内容“看起来”变了。
# 修改内部列表后t: (1, 2, [3, 4, 5]), id: 2531938380352

## 可变数据类型

# 列表 (list)
my_list = [1, 2, 3]
print(f"初始my_list: {my_list}, id: {id(my_list)}") # 初始my_list: [1, 2, 3], id: 1647392761792
my_list.append(4)  # 直接修改原列表
print(f"append后my_list: {my_list}, id: {id(my_list)}") # append后my_list: [1, 2, 3, 4], id: 1647392761792
my_list[0] = 99    # 直接修改原列表的元素
print(f"修改元素后my_list: {my_list}, id: {id(my_list)}") # 修改元素后my_list: [99, 2, 3, 4], id: 1647392761792

# 字典 (dict)
my_dict = {'a': 1, 'b': 2}
print(f"初始my_dict: {my_dict}, id: {id(my_dict)}") # 初始my_dict: {'a': 1, 'b': 2}, id: 1647399873088
my_dict['c'] = 3  # 直接修改原字典
print(f"添加键值对后my_dict: {my_dict}, id: {id(my_dict)}") # 添加键值对后my_dict: {'a': 1, 'b': 2, 'c': 3}, id: 1647399873088

# 集合 (set)
my_set = {1, 2, 3}
print(f"初始my_set: {my_set}, id: {id(my_set)}") # 初始my_set: {1, 2, 3}, id: 1647397072768
my_set.add(4)     # 直接修改原集合
print(f"add后my_set: {my_set}, id: {id(my_set)}") # add后my_set: {1, 2, 3, 4}, id: 1647397072768