# %%
a=input()
b=0
a=a.lower()
for i in a:
    if i in ['a','e','i','o','u']:
      b+=1
print(b)

# %%
a=list(map(int, input().split()))
b=0
c=0
for i in a:
  if i%2==0:
    b+=i
  else:
    c+=i
print(b)
print(c)

# %%
a=int(input())
b=0
for i in range(1,a+1):
  if i%3==0:
    b+=i
print(b)


# %%
a=input()
if a==a[::-1]:
  print("회문입니다.")
else:  
  print("회문이 아닙니다.")

# %%
a=input().split()
for i in a:
  print(len(i))


# %%
a=input()

h_a=False
h_d=False
for i in a:
  if i.isalpha():
    h_a=True
  elif i.isdigit():
    h_d=True
if h_a==True and h_d==True and len(a)>=8:
  print("사용가능")
else:  
  print("사용불가")



# %%

nu = list(map(int, input("숫자들을 입력하세요: ").split()))
m = nu[0]
min = nu[0]
for n in nu:
    if n > m:
        m = n
    if n < min:
        min = n
print("최댓값:", m)
print("최솟값:", min)


# %%

a = int(input("학생 수를 입력하세요: "))

scores = []
b = 0
for i in range(a):
    score = int(input())
    scores.append(score)
    if score >= 80:
        b += 1
print(f"평균 점수: {sum(scores) / a:.1f}")  
print(f"80점 이상 학생 수: {b}명")

# %%
a=list(map(int, input().split()))
a=list(set(a))
a.sort()
print(a)

# %%
a=int(input())
b={}
t=0
for i in range(a):
  n,s=input().split()
  b[n]=s
  t+=int(s)
  avg=t//a
for n,s in b.items():
  if int(s)>=avg:
    print(n,s)

# %%
a=input().split()
b={}
for i in a:
  if '.' in i:
    e=i.split('.')[1].lower()
    if e in b:
      b[e]+=1
    else:
      b[e]=1
for e,c in b.items():
  print(f"{e}: {c}회")


# %%
#12
a=input()
r=''
c=1
for i in range(1,len(a)):
  if a[i]==a[i-1]:
    c+=1
  else:
    r+=a[i-1]+str(c)
    c=1
r+=a[-1]+str(c)
print(r)

# %%
a=list(map(int, input().split()))
k=int(input())
n=len(a)
r=a[-k:]+a[:-k]
print(r)


# %%
a=int(input())
i_p=True
for i in range(2,a):
  if a%i==0:
    i_p=False
    break
if i_p:
  print("소수")
else:  
  print("소수 아님")

# %%
for i in range(2,10):
  for j in range(1,10):
    k=i*j
    if k % 2==0:
      print(i, 'x', j, '=', k)



# %%
a=input().split()
print(a)
s=''
for i in a:
  if len(i)>len(s):
    s=i
print(s)
  

# %% [markdown]
# 


