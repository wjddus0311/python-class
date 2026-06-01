# %%
#15
a,b=input().split(":")
print(a,b,sep=":")

# %%
y,m,d=input().split(".")
print(d,'-',m,'-',y,sep='')

# %%
a,b=input().split('-')
print(a,b,sep='')


# %%
a=input()
print(a[0])
print(a[1])
print(a[2])
print(a[3]) 
print(a[4])

# %%
a=input()
print(a[0:2],a[2:4],a[4:6] ,sep=' ')

# %%
a=input().split(':')
print(int(a[1]))

# %%
a,b=input().split(' ')
c=a+b
print(c)

# %%
a,b=input().split(' ')
c=int(a)+int(b)
print(c)

# %%
a=float(input())
b=float(input())
c=a+b
print(c)

# %%
a=int(input())
print("%x" %a)

# %%
a=int(input())
print("%X" %a)

# %%
a=(input())
n=int(a,16)
print("%o" %n)

# %%
n=ord(input())
print(n)

# %%
a=int(input())
print(chr(a))

# %%
a=int(input())
print(-a)

# %%
a=input()
print(chr(ord(a)+1))

# %%
a,b=input().split(' ')
c=int(a)-int(b)
print(c)

# %%
a,b=input().split(' ')
c=float(a)*float(b)
print(c)

# %%
a,b=input().split(' ')
c=a*int(b)
print(c)

# %%
a=input()
b=input()
print(int(a)*b)

# %%
a,b=input().split(' ')
c=int(a)**int(b)
print(c)

# %%
a,b=input().split(' ')
c=float(a)**float(b)
print(c)

# %%
a,b=input().split(' ')
c=int(a)//int(b)
print(c)

# %%
a,b=input().split(' ')
c=int(a)%int(b)
print(c)

# %%
a=float(input())
print(round(a,2))

# %%
a,b=input().split(' ')
c=float(a)/float(b)
print(round(c,3))

# %%
a,b=map(int,input().split(' '))
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
c=a/b
print(round(c,2))

# %%
a,b,c=map(int,input().split(' '))
d=(a+b+c)/3
print((a+b+c),round(d,2))

# %%
a=int(input())
print(a<<1)

# %%
a,b=map(int,input().split(' '))
print(a<<b)

# %%
a,b=map(int,input().split(' '))
if a<b:
    print(True)
else:
    print(False)

# %%
a,b=map(int,input().split(' '))
if a==b:
    print(True)
else:
    print(False)

# %%
a,b=map(int,input().split(' '))
if a<=b:
    print(True)
else:
    print(False)

# %%
a,b=map(int,input().split(' '))
if a!=b:
    print(True)
else:
    print(False)

# %%
a=(int(input()))
print(bool(a))

# %%
a=bool(int(input()))
print(not(a))

# %%
a,b=input().split()
print(bool(int(a))and bool(int(b)))

# %%
a,b=input().split()
print(bool(int(a)) or bool(int(b)))

# %%
a,b=input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))

# %%
a,b=input().split()
c = bool(int(a))
d = bool(int(b))
print( c==d)

# %%
a,b=map(int,input().split())
c = bool(a)
d = bool(b)
print(not a and not b)


# %%
a, b = input().split()
a = int(a)
b = int(b)
c = (a if (a>=b) else b)
print(int(c))

# %%
#61
a,b,c = input().split()
print((a if a<b else b) if ((a if a<b else b)<c) else c)

# %% [markdown]
# 


