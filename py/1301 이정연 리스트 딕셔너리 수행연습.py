# %%
#1
a=input()
if a==a[::-1]:
  print('펠렌드롬입니다')
else:
  print('펠렌드롬이 아닙니다')




# %%
a=input()
is_p=True
for i in range(0,len(a)//2):
  if a[i] != a[-1-i]:
    is_p=False
    break
if is_p:
  print('펠렌드롬입니다')
else: 
  print('펠렌드롬이 아닙니다')


# %%
#2-1
nums = [10, 15, 13, 20]
n = 0
for i in nums:
    if n == 0:
        n = i
    else:
        print(i - n, end=' ')
        n = i

# %%
#2-2
nums = [10, 15, 13, 20]
l = len(nums)
n = 0
for i in range(0,l):
    if n == 0:
        n = nums[i]
    else:
        print(nums[i] - n, end=' ')
        n = nums[i]

# %%
#3
nums = [5, 7, 3, 8, 10]
n = nums[0]
for i in range(1, len(nums)):
    if nums[i] > n:
        print(nums[i], end=' ')
    n = nums[i]

# %%
#4
a={}
while True:
  b=input()
  if b=='q':
    break
  n,s=b.split()
  a[n]=int(s)

for n,s in a.items():
  if s>=80:
    print(n, '합격')
  else:
    print(n,'불합격')
# for n in a:
#   if a[n]>=80:
#     print(n, '합격')
#   else:
#     print(n,'불합격')



  
  
  




# %%
#5
c = int(input())
stu = []
high = 0
low = 10**20
total = 0
for i in range(c):
    o = int(input())
    stu.append(o)

for i in stu:
    total += i
    if i > high:
        high = i
    if i < low:
        low = i
print('총점:', total)
print('평균:', int(total/c))
print('최고:', high)
print('최저:', low)

# %%
#6
b={}
a=input()
for i in range(int(a)):
  a,s=input().split()
  b[a]=int(s)
  na=None
  m=-1
  for a,s in b.items():
    if s>m:
      m=s
      na=a
  print(na,m)
  
  for a in b:
    if b[a]>m:
      m=b[a]
      na=a
  print(na,m)


# %%
a=input()
seen=set()
dup=set()
for i in a:
  if i in seen:
    dup.add(i)
  else:
    seen.add(i)
print(dup)


# %%
words =input().split()
result={}
for w in words:
  w=w.lower()
  if w in result:
    result[w]+=1
  else:
    result[w]=1
for i in result:
  print(i,result[i])


# %%
words =input().split()
result={}
for w in words:
  w=w.lower()
  result[w]=result.get(w,0)+1
for k,v in result.items():
  print(k,v)  

# %%
w=input()
n={'alpha':0,'digit':0,'special':0}
for i in w:
  key=i.lower()
  if key.isalpha():
    n['alpha']+=1
  elif key.isdigit():
    n['digit']+=1
  else:
    n['special']+=1
print(n)

# %%
a=input().split()
b=list(map(int,input().split()))
c={}
for i in range(len(a)):
  c[a[i]]=b[i]
print(c)


# %%
a=input().split()
b=list(map(int,input().split()))
c={}
for i,j in zip(a,b):
  c[i]=j
print(c)

# %%
fruits = input().split()
prices=list(map(int,input().split()))
c={}
for i,j in zip(fruits,prices):
  c[i]=j
print(c)

# %%
fruits = input().split()
prices=list(map(int,input().split()))
c={}
for i,j in zip(fruits,prices):
  c[i]=j
for k,v in c.items():
  print(k,'의 가격은 ', v,'원 입니다.')

# %%
fruits = input().split()
prices=list(map(int,input().split()))
c={}
for i,j in zip(fruits,prices):
  c[i]=j
sales_box={}
for k,v in c.items():
  sales_box[k]=v*0.9
print(sales_box)

# %%
a=input().split()
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d={}
for i,j,k in zip(a,b,c):
  avg=(j+k)/2
  print(f'{i}의 평균 점수는 {avg}')


# %%
old_dict={"A":1,"B":2,"C":3}
n={}
for i,j in old_dict.items():
  n[j]=i
print(n)

# %%



