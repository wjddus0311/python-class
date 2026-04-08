import random as r
a=(input("가위 바위 보"))
print(a)
b=['가위','바위','보']
c=r.choice(b)
print(r.choice(b))
if a=="가위":
    if c=='보':
        print('승리')
    elif c=='바위':
        print('패배')
    elif a==c:
        print('비겼습니다')

import random as r
print(r.randint())