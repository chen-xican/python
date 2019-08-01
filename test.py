# 直接修改数据集（ds）
arr = {}
data = [{'id': 'a', 'value': 1}, {'id': 'a', 'value': 3}, {'id': 'b', 'value': 2}]
for row in data:
    temp = row['id']
    if (temp in arr):
        arr[temp] += row['value']
    else:
        arr[temp] = row['value']
print(arr)


