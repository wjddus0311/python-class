# %%
py='python programming'
print(py.count('p'))
print(py.find('o'))
print(py.index('o'))
print(py.find('z'))
#print(py.index('z')) 인덱스 함수는 특정 문자 값이 없을시 오류가 남

# %%
py='Python'
print(py.upper())
print(py.lower())

# %%
py= '파이썬 공부는 너무 재미있어요!'
print(py.replace('파이썬','자바'))
print(py)

# %%
py='파이썬 공부는 너무 재미있어요!'
print(py.split(' '))
print(py.split())
print(py)

# %%
a='1:2:3:4'
print(a.split(':'))


# %%
print((100>10)or(30<3))
print((10==10)and (3!=3))
print(not (3<3))

# %%
con='sweet'
if con=='sweet':
    print('삼키다')
else:
    print('뱉는다')

# %%
season='summer'
if season == 'spring':
    print('꽃이 펴요')
else:
    if season=='summer':
        print('여름에는 더워요~')
    else:
        if season=='fall':
            print('가을은 독서의 계절!')
        else:
            if season=='winter':
                print('겨울에는 눈이 와요~')

# %%
a=int(input('점수를 입력해주세요'))
if a >= 70:
    print('합격')
    if a >= 90:
        print('장학금대상')
else:
    print('재도전')

# %%
temp=18
if temp<26:
    pass
else:
    print('에어컨을 켠다')

# %%
n=input('숫자를 입력하세요:')
if '3' in n or '6' in n or '9' in n:

    print('박수 짝')
else:
    print('369숫자가 아닙니다')

# %%
i=1
while i<=5 :
    print(i,'hello')
    i=i+1

# %%
i=0
while i+1<=5:
    print(i+1,'hello')
    i=i+1

# %%
i = 1
while i<11:
    print('파이썬'+str(i))
    i=i+1

# %%
i=1
total=0
while i<=5:
    print(i)
    total=total+i
    i=i+1
print('1~5까지의 합은',total)


# %%



