# coding:UTF-8
# t = (2,4,6)
# def a(t):
#     t+=(9,10)
# a(t)
# print(t)
# print(t)


# def makebold(fn):
#     def ss():
#         return "<b>" + fn() + "</b>"

# def makeitalic(fn):
#     def aa():
#         return "<i>" + fn() + "</i>"
   

# @makebold
# @makeitalic
# def hello():
#     return "hello world"

# print(hello()) ## returns "<b><i>hello world</i></b>"


# 阶乘
# def jie(a):
#     if a == 2:
#         return 0
#     return 7+jie(a-1)

# print(jie(6))

# 2  0
# 3  7
# 4  14
# 5-2   21
# 6-2 *7 28

# a = map(lambda x:x*2,[1,2,3])
# print(a)
# for ch in a:
#     print(ch)


# import copy
# a = [1, 2, 3, 4, ['a', 'b']]  #原始对象

# b = a  #赋值，传对象的引用
# c = copy.copy(a)  #对象拷贝，浅拷贝
# d = copy.deepcopy(a)  #对象拷贝，深拷贝

# a.append(5)  #修改对象a
# a[4].append('c')  #修改对象a中的['a', 'b']数组对象

# print('a = ', id(a))
# print('b = ', id(b))
# print('c = ', id(c))
# print('d = ', id(d))

# a = 5
# b = a
# c = a == 2*b
# print(c)
# print('a = ', id(b))
# print('b = ', id(b))
# l1 = (x for x in range(100)]
# print(l1)
# n = 1
# while n<=20:
#     print(next(l1))
#     n+=1
# for x in l1:
#     if x<=10:
#         print(x)
def makebold(fn):
    def wrapped():  
        return "<b>" + fn() + "</b>"  
    return wrapped  
   
def makeitalic(fn):  
    def wrapped():  
        return "<i>" + fn() + "</i>"  
    return wrapped  
  
@makebold  
@makeitalic  
def hello():  
    return "hello world"  
print(hello())



