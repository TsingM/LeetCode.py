'''
方法一：原字符串替换
'''
def defangIPaddr(address: str) -> str:
    arr = list(address)
    for i in range(len(arr)):
        if arr[i] == '.':
            print(' ')
            arr[i] = '[' + arr[i] + ']'
    return ''.join(arr)

'''
方法二：新字符串填充
'''
def defangIPaddr(address: str) -> str:
    arr = ''
    for a in address:
        if a == '.':
            arr += '[.]'
        else:
            arr += i
    return arr

print(defangIPaddr('1.1.1.1'))