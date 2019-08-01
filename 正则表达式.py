import re

re.match(r'\d{3}\-\d{3,8}$', '010-12345')  # 匹配到返回match 对象 匹配不到返回none
re.split(r'\s+', 'a b    c')
re.split(r'[\s\,]+', 'a,b,c d ')
re.split(r'[\s\,\;]+','a,c;f;s,f;;s')
