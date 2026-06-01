 # %%
#1
a=input()
b=input()
c=input()
d=input()
sum = sum1 = sum2 = sum3 = 1
if b == 'T' and a == 'F' :
    sum = 0
if a == 'T' and d == 'T':
    sum1 = 0
if a == 'F' and b == 'T':
    sum2=0
if b != d:
    sum3=0
if sum==1 and sum1==1 and sum2==1 and sum3==1:
    print('조건만족')
else:
    print('조건불만족')
# %%
#2
a=int(input('키를 입력하세요:'))
b=input('보호자 동반이신가요?')
c=int(input('나이를 입력하세요'))
d=input('직원이 있나요?')
e=input('안전교육 이수했나요?')

if c >= 65:
    print('탑승불가')
elif d == 'T' and e == 'F':
    print('탑승불가')
elif a >= 140 or d == 'T':
    print('탑승 가능')
elif 120 <= a < 140 and b == 'T':
    print('보호자 동반 시 가능')
else:
    print('탑승불가')

# %%
#3
c=0
t=0
while True:
    s=int(input())
    if s==-1:
        break
    if 0<=s<=100:
        t+=s
        c+=1
    else:
        print('잘못된 결과')
if c > 0:
    a = t / c
    print("평균:", a)
else:
    print("입력된 점수가 없습니다")



# %%
has_ex=False
has_n=False
while True:
    p=input('비밀번호')
    for i in p:
        if i=='!':
            has_ex=True
        if i.isdigit():
            has_n=True
    if len(p)>=8 and has_ex and has_n:
        print('사용가능')
        break
    else:
        print('잘못 입력')

# %%
#5                                                              
e=0
for i in range(1,201):
    if i%28==0:
        continue
    elif i%4==0:
        e+=4
    elif i%7==0:
        e+=7
print("총 에코 포인트:",e)

# %%
#6
for i in range(1,6):
    for j in range(5-i):
        print(' ',end='')
    for j in range(1,1+i):
        print(j,end='')
    for j in range(i-1,0,-1):
        print(j,end="")
    print()


