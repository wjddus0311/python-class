# %%
"""
작성자 : 홍길동
수정날짜 : 3월 9일
"""
print('소마고')#학교이름

# %%
name = input('이름을 입력하세요')
age = int(input('나이를 입력하세요'))
print('제 이름은',name,'이고, 나이는',age,'세 입니다.')

# %%
a=int(input('첫번째 수를 입력하세요'))
b=int(input('두번째 수를 입력하세요'))
print('두 숫자의 곱은',a*b,'입니다.')

# %%
a=int(input('섭씨를 입력하시오:'))
b=a*1.8+32
print('섭씨',a,'도는 화씨',b,'도 입니다.')

# %%
var=7
print(type(var))

# %%
j=3.14
print(type(j))

# %%
print(bool(1)) #값이 존재함
print(bool(0)) # 값이 존재하지 않음
print(bool(None)) #값이 존재하지 않음
print(bool('')) #값이 존재하지 않음
print(bool('python')) #값이 존재함
#bool은 값이 존재할때 true 존재 하지 않을때 false

# %%
print('''동해물과
      백두산이
            마르고



                닳도록''')

# %%
i='python'
j='string'
print(i+j)
print(i*3)

# %%
py="파이썬으로 코딩을 배우자!"
print(py[0])
print(py[6])
print(py[-1])
print(len(py))

# %%
korea='우리집 강아지 이름은 멍멍이입니다.'
print(korea[4])
print(korea[4:7])
print(korea[:4])
print(korea[4:])

# %%
a='가나다라마바사'
print(a[:4])
print(a[2:5])


