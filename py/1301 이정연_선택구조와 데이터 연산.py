# %%
#1번
score = input('성적을 입력하시오:')
score=int(score)
if score >= 60:
    print('합격')
else:
    print('불합격')

# %%
#2번
card=int(input("카드 잔액을 입력하세요:"))
if card >= 1000:
    print('버스 탑승 가능')
else:
    print('버스 탑승 불가')

# %%
#3
capt=input('보안 문자 입력하세요:')
if capt=='N8SHA':
    print('비밀번호 찾기 허용')
else:
    print('비밀번호 찾기 허용 안 함.')

# %%
#4
base=270
use=int(input('전기 사용량(kW)입력:'))
if use>100:
    cost=use*base*1.1
else:
    cost=use*base
print('전기 사용량:',use,'kW')
print('전기 요금:',cost,'원')

# %%
#5
id=input('id를 입력하세요:')
pwd=input('pwd를 입력하세요:')
if id=='info' and pwd=='edu':
    print('로그인 되었습니다.')
else:
    print('로그인에 실패했습니다.')

# %%
#6
kind=input('당신의 승객 유형은?[임산부, 노약자, 일반]')
if kind=='임산부'or kind=='노약자':
    print('이용 가능')
else:
    print('이용 불가능')

# %%
#7
kind=input('당신의 승객 유형은?[임산부,노약자,일반]')
if not kind=='일반':
    print('이용 가능')
else:
    print('이용 불가능')

# %%
#8
p=input('점수를 입력하세요.')
p=int(p)
if p >= 90:
    print('A')
elif p>=80:
    print('B')
elif p>=70:
    print('C')
else:
    print('D')

# %%
#9
n=int(input('정수를 입력하세요:'))
if n%2==0:
    print('짝수입니다')
else:
    print('홀수입니다')

# %%
#10
n=int(input('정수를 입력하세요:'))
if n>0:
    print('양수입니다')
elif n==0:
    print('0입니다')
else:
    print('음수입니다')

# %%
#11
age=int(input('나이를 입력하세요:'))
cost=14000
if age>=60:
    cost=14000*0.7
elif age<=10:
    cost=14000*0.8
else:
    print('할인 대상이 아닙니다')
print('찜질방 이용 요금:',cost)

# %%
#12
n1=int(input('첫번째 정수:'))
n2=int(input('두번째 정수:'))
if n1>n2:
    print(n1,'이(가) 더 큽니다')
elif n1==n2:
    print(n1,'과',n2,'의 값은 같습니다')
else:
    print(n2,'이(가) 더 큽니다')

# %%
#13
a=int(input('점수를 입력하세요:'))
if a>=60:
    print('합격')
    if a>=90:
        print('장학금 대상')
else:
    print('불합격')

# %%
#11
age=int(input('나이를 입력하세요:'))
cost=14000
if age>=60 or age<=10:
    if age>=60:
        cost=14000*0.7
    if age<=10:
        cost=14000*0.8
else:
    print('할인 대상이 아닙니다')
print('찜질방 이용 요금:',cost)   


