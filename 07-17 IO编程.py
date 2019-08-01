# try:
#     f = open('E:/111.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
# ---------------------------
# with open('E:/111.txt','r') as f:
#     print(f.read())

# with open('E:/111.txt','rb') as f:  #rb 读取16进制字符
#     print(f.read())

import os

# print(os.name)
# print(os.environ.get("path"))#获取环境变量

# 查看当前文件的绝对路径
# print(os.path.abspath('.'))
# 拼接路径
file = os.path.join(os.path.abspath('.'), 'haha')
# 创建文件夹
# os.mkdir(file)
# 删除文件夹
# os.rmdir(file)
# 分割路径 splittext 直接得到文件的扩展名
# print(os.path.split(file))
# os.rename  重命名文件  os.remove 删除文件
# 获取当前目录下的所有文件夹
# print([x for x in os.listdir('.') if os.path.isdir(x)])
# 获取当前所有.py文件
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
# print([x for x in range(0, 10) if (x != 11)])
from io import StringIO

f = StringIO()
len = f.write('hello')
print(len)
f.write(' ')
f.write('world')
print(f.getvalue())
