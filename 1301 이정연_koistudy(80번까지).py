# %%
a, b, c = map(int, input().split())
print(a if a < b and a < c else (b if b < c else c))

# %%
a, b, c = map(int, input().split())
if a%2==0:
    print(a)
if b%2==0:
    print(b)
if c%2==0:
    print(c)


# %%
a, b, c = map(int, input().split())
if a%2==0:
    print('even')
else:
    print('odd')

if b%2==0:
    print('even')
else:
    print('odd')
if c%2==0:
    print('even')
else:
    print('odd')

# %%
n = int(input())

if n < 0:
    if n % 2 == 0:
        print("A")
    else:
        print("B")
else:
    if n % 2 == 0:
        print("C")
    else:
        print("D")

# %%
n=int(input())
if n>=90:
    print('A')
elif n>=70:
    print('B')
elif n>=40:
    print('C')
else:
    print('D')

# %%
n=(input())
if n=='A':
    print('best!!!')
elif n=='B':
    print('good!!')
elif n=='C':
    print('run!')
elif n=='D':
    print('slowly~')
else:
    print('what?')

# %%
n=int(input())
if n//3==0 or n//3==4:
    print('winter')
elif n//3==1:
    print('spring')
elif n//3==2:
    print('summer')
else:
    print('fall')

# %%
n=1
while n!=0:
    n=int(input())
    if n!=0:
        print(n)


# %%
n=int(input())
while n!=0:
    n=n-1
    print(n)
    if n>100:
        break


# %%
c = ord(input())
t = ord("a")
while t<=c :
    print(chr(t), end=" ")
    t += 1

# %%
a = int(input())
b=int('0')
while b<=a:
    print(int(b))
    b += 1

# %%
n = int(input())
for i in range(n+1):
    print(i)

# %%
n=int(input())
s=0
for i in range(1,n+1):
    if i%2==0:
        s+=i
print(s)

# %%
while True:
    ch = input()
    print(ch)
    if ch == 'q':
        break

# %%
n = int(input())
s = 0
i = 0
while s < n:
    i += 1
    s += i

print(i)

# %%
n,m= map(int, input().split())
for i in range(1,n+1):
    for j in range(1,m+1):
        print(i,j)

# %%
n=int(input(),16)
for i in range(1,16):
    print("%X" % n, "*%X" % i, "=%X" % (n*i), sep="")

# %%
n = int(input())

for i in range(1, n+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        print("X", end=" ")
    else:
        print(i, end=" ")

# %%
r,g,b= map(int, input().split())
check=0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k)
            check+=1
print(check)



