print('-----------------1.高阶函数map----------------')
import time,os,functools,sys
from functools import reduce


def f(x):
    return x * x


print(list(map(f, [1, 2, 3, 4, 5, 6])))


def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))
print(sum([1, 3, 5, 7, 9]))
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)


def pStr(x, y):
    return x * 10 + y


print(reduce(pStr, [1, 2, 3, 4]))


def normalize(name):
    return name[0].upper() + name[1:].lower()


l1 = ['adam', 'LISA', 'barT']

l2 = map(normalize, l1)

print(list(l2))

print('*****************')


def prod(L):
    def pro(x, y):
        return x * y

    return reduce(pro, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
print('***************************')


def str2float(s):
    def fn1(x, y):
        return 10 * x + y

    def fn2(x, y):
        return 0.1 * x + y

    def char2num(s):
        di = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
        return di[s]

    index = s.index('.')
    return reduce(fn1, map(char2num, s[0:index])) + reduce(fn2, map(char2num, s[:index:-1])) / 10


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

print('-----------------2.高阶函数filter----------------')

print('一、**************************************')


def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 9, 10, 15])))
print('二、**************************************')


def del_null(n):
    return n and n.strip()


print(list(filter(del_null, ['A', '', 'B', None, 'C', '  '])))
print('三、**************************************')


def is_palindrome(n):
    return str(n) == str(n)[::-1]


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

print('-----------------3.高阶函数sorted----------------')

print('一、**************************************')
print(sorted([36, 5, -12, 9, -21], key=abs))
print('二、**************************************')
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
print('三、**************************************')
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


L2 = sorted(L, key=by_name)
print(L2)
print('四、**************************************')
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_score(t):
    return -t[1]


L2 = sorted(L, key=by_score)
print(L2)

print('-----------------4.返回函数----------------')

print('**************************************')


def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()

print(f1(), f2(), f3())

print('-----------------5.匿名函数----------------')
print('一、匿名函数lambda **************************************')


def is_odd(n):
    return n % 2 == 1


L = list(filter(lambda n: n % 2 == 1, range(1, 20)))

print(L)

print('-----------------6.装饰器----------------')
print('1.************************************')


def log(text, text2):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s %s():' % (text, text2, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('调用', os.path.basename(sys.argv[0]))
def now():
    print('2015-3-25')


print('-----------------7.偏函数----------------')

max2 = functools.partial(max, 20)
int2 = functools.partial(int, base=2)
print(max2(1, 2, 5, 7, 9, 12, 3.4))
print(int2('101010'))
