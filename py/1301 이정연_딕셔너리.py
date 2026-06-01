# %%
stu1 = {'학반':105,'번호':20,'이름':'홍길동'}
print(stu1)
stu1['연락처']='010-1111-2222'
print(stu1)
stu1['동아리']='파이썬 동아리'
print(stu1)
del stu1['연락처']
print(stu1)
print(stu1['이름'])
print(stu1.get('이름'))
#print(stu1['주소'])
print(stu1.get('주소'))
print(stu1.keys())
print(list(stu1.keys()))
print(stu1.values())
print(list(stu1.values()))
print('이름' in stu1)
print('주소' in stu1)

# %%
w=['aaa','Daegu','web']
person={'name':'aaa','address':'Daegu','interest':'web'}
print(person)
print(person['name'])

for key in person:
  print(key,person[key])

# %%
persons=[{'name':'aaa','address':'Daegu','interest':'web'},{'name':'bbb','address':'Seoul','interest':'IOT'},{'name':'ccc','address':'LA','interest':'web'}]
print('====persons====')
for person in persons:
  print('------------')
  for key in person:
    print(key,':',person[key]) #key value 출력 방법


# %%
t=(1,2,3)
print(t[0])

# %%
t=(1,2,3)
print(t[1:3])

# %%
t=('a','b','c')
for x in t:
  print(x)

# %%
t=(1,2,3)
print(t*2)

# %%
t=(10,20,30)
print(t[1:3])

# %%
score={'민수':90,'지영':80}
print(score['민수'])

# %%
score={'민수':90}
score['지영']=85
print(score)

# %%
score={'민수':90}
print(score.get('민수'))

# %%
score={'민수':90}
if '민수' in score:
  print('있다')

# %%
score={'민수':90,'지영':80}
for k in score:
  print(score[k])

# %%
score={'민수':90,'지영':80}
for k,v in score.items(): #키와 값을 한번에 꺼내옴
  print(k,v)

# %%
score={'민수':90,'지영':80}
print(score.keys())

# %%
score={'민수':90,'지영':80}
print(score.values())


# %%
score={'민수':90,'지영':80}
del score['지영']
print(score)

# %%
score={'민수':90,'지영':80}
score['민수']=100
print(score)

# %%
score={'민수':90,'지영':75,'철수':82}
for name in score:
  if score[name] >= 80:
    print(name)

# %%
menu={'김밥':3000,'라면':4000}
food = '김밥'
if food in menu:
  print(menu[food])

# %%
score={'민수':90,'지영':80}
total=0
for v in score.values():
  total += v
print(total)

# %%
words = ['a','b','a']
result={}
for w in words:
  if w in result:
    result[w]+=1
  else:
    result[w]=1
print(result)


# %%
score={'민수':90,'지영':75,'철수':82}
m=0
n=''
for key in score:
  if score[key] > m:
    m=score[key]
    n=key
print(n,m)

# %%
score={'민수':95,'지영':82,'철수':68}
for key in score:
  if score[key] >= 90:
    score[key]='A'
  elif score[key] >= 80:
    score[key]='B'
  else:
    score[key]='C'
print(score)

# %%
#22
words=['apple','banana','kiwi']
result={}
for key in words:
  result[key]=len(key)
print(result)


# %%
nums=[1,2,2,3,3,3]
nums=set(nums)
print(tuple(nums))

# %%
#20
score={'민수':90,'지영':75,'철수':82}
m=0
n=''
for i, j in score.items():
  if j > m:
    m=j
    n=i
print(n,m)

# %%
#21
score={'민수':95,'지영':82,'철수':68}
d={}
for i in score:
  if score[i] >=90:
    d[i]='A'
  elif score[i] >=80:
    d[i]='B'
  else:
    d[i]='C'
print(score)
print(d)


