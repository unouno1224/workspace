# 파이썬 연습1 2018-03-13
import math
# import urllib.request as rq
from urllib.request import urlopen

a,b=input('문자를 2개 입력하세요 :  ').split()
if (a=='숫자' and b=='10'):
    print('와우 {}가 {}네요.'.format(a,b))
    print('if탔군...')
else:
    print(a+'는',b+'입니다.')
print('자연상수 e는'+str(math.e))
print(math.sqrt(4))
response = urlopen('http://www.naver.com')
print(response.status)
