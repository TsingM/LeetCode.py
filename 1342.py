'''
方法一：普通条件判断
'''
def numberOfSteps (num):
    output = 0
    while num > 0:
        output += 1
        if num % 2 == 0:
            num = num / 2
        else:
            num -= 1
    return output

'''
方法二：递归
'''
def numberOfSteps (num):
    step = 0
    output = reduceToZero(num, step)
    return output
def reduceToZero(num, step):
    return step if num <= 0 else reduceToZero(num = num / 2 if num % 2 == 0 else num - 1, step = step + 1)

print(numberOfSteps(123))