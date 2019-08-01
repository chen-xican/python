# try:
#     print('try...')
#     r = 10 / 0
#     print('result', r)
# except ZeroDivisionError as e:
#     print('except', e)
# finally:
#     print('finally...')
# print('END')
# --------------------------------------
# try:
#     print('try...')
#     r = 10 / int('a')
#     print('result', r)
# except ValueError as e:
#     print('ValueError', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionErr', e)
# finally:
#     print('finally...')
# print('END')
# -------------------------------
from globalLog import ta_log


#
# def foo(s):
#     return 10 / int(s)
#
#
# def bar(s):
#     return foo(s) * 2
#
#
# def main():
#     try:
#         bar('0')
#     except  Exception as e:
#         ta_log.exception(e)
#
#
# main()
# print('END')
#
# import pdb
# def foo(s):
#     pdb.set_trace()
#     n = int(s)
#     pdb.set_trace()
#     assert n != 0, 'n is zero!'
#     return 10 / n
#
#
# def main():
#     foo('0')
#
# main()
# ---------------------------------------------
