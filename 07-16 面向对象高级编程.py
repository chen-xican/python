# class Student(object):
#     pass
# s=Student()
# s.name = 'Michael'
# print(s.name)
#
# def set_age(self,age):
#     self.age = age
# from types import MethodType
#
# s.set_age = MethodType(set_age,s)
# s.set_age(25)
# print(s.age)
#
# s2 =Student()
# # s2.set_age(24) # s 的实例方法对s2是不起作用的
#
# def set_score(self,score):
#     self.score=score
# Student.set_score = set_score
# s.set_score(100)
# print(s.score)
#
# s2.set_score(99)
# print(s2.score)

# class Student(object):
#     __slots__ = ('name','age')
# s=Student()
# s.name='Michael'
# s.age=25
# s.score=99  #添加这个属性是没办法成功的 __slots__ 对继承子类是不起作用固定

#------------------------------
# class Student(object):
#
#     @property
#     def birth(self):
#         return self._birth
#
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
#
#     @property
#     def age(self):
#         return 2015 - self._birth
# s=Student()
# s.birth = 20
# print(s.age,s.birth)
#------------------测试
# -*- coding: utf-8 -*-
# class Screen(object):
#     @property
#     def width(self):
#         return self._width
#     @width.setter
#     def width(self,value):
#         self._width=value
#
#     @property
#     def height(self):
#         return self._height
#     @height.setter
#     def height(self,value):
#         self._height=value
#
#     @property
#     def resolution(self):
#         return self._width*self._height
#
#
# # 测试:
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')
# ---------------------
# class Student(object):
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return 'Student object (name: %s)'% self.name
# print(Student('Michael'))
#--------------------
# from enum import Enum
#
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# -------------------------------------------