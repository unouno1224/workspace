#%%
def is_int(x):
    try:
        if int(x)==x:
            return True
        else: return False
    except ValueError:
        return False
print (is_int(-3.4))
print (is_int('aafdf'))
print (is_int(-2.0))

def digit_sum(x):
    total = 0
    for i in str(x):
        total += int(i)
    return total
print (digit_sum(23414))

def is_prime(x):
    try:
        x=int(x)
    except: 
        ValueError
        return '2이상의 정수를 입력하세요'
    if x<2:return '2이상의 정수를 입력하세요'
    for i in range(2,x):
        if x % i == 0:
            return '합성수'
    else:
        return '소수'
x = input('소수판별기, 정수로 입력하세요 :')
print (is_prime(x))
print ('abcde!@#$%'[::-1])
print (type(range(6)))
print ('abcde!@#$%'.strip('ae'))
