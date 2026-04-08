# %%
s = 0 #합계
while True:
    nn=input('숫자 입력 (종료는 n):')

    if nn=='n':
        break
    s=s+int(nn)

print('합계:',s)
    

# %%
#1
i=1
while i<=5:
    print('hello world')
    i=i+1

# %%
#2
i=1
s=0
while i<=5:
    print(i)
    s=s+i
    i=i+1

print('1~5까지의 합은',s)

# %%
#3
s=0
while s<=20:
    n=int(input('숫자 입력:'))
    s=s+n
print('입력한 수의 합은:',s)


# %%
#4
h=0
while h<=20:
    n=int(input('숫자 입력:'))
    h=h+n
    if h>20:
        break
print('입력한 수의 합은:',h)

# %%
#5
p=0
s=0
while s<=20:
    p=int(input('다트 점수를 입력하세요:'))
    print('이번 점수는',p)
    s=s+p
print('합계 점수는',s)

# %%



