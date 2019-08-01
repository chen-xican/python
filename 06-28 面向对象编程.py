# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print("%s %s" % (self.name, self.score))
#
#
# bart = Student('chenxican', 59)
# bart.print_score()


class Student(object):
    def __init__(self, score, name):
        self.__score = score
        self.__name = name

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 80:
            return 'B'
        else:
            return 'C'

    def get_NameAndScore(self):
        print('%s考了%d分' % (self.__name, self.__score))


bart = Student(89, 'chenxican')
print(bart.get_grade())
bart.get_nameAndScore()

# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender
#     def get_gender(self):
#         return self.__gender
#     def set_gender(self,gender):
#         self.__gender=gender
#
# # 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')
#
# class Student(object):
#     count = 0
#     def __init__(self, name):
#         self.name = name
#         Student.count+=1
#
# # 测试:
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')
