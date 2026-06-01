# %%
#1
class Person:
  def __init__(self,name):
    self.name=name
p1=Person('홍길동')
p2=Person('이순신')

print(p1.name)
print(p2.name)

# %%
#2
class Animal:
  def __init__(self,name,age):
    self.name=name
    self.age=age
dog=Animal('강아지',3)
print(dog.name,dog.age)

# %%
#3
class Monster:
  def __init__(self,name):
    self.name=name
  def say(self):
    print(f'나는 {self.name}')
dragon=Monster('드래곤')
dragon.say()

# %%
#4
class Student:
  def __init__(self,name,score):
    self.name=name
    self.score=score

s1=Student('철수',80)
s2=Student('영희',90)
s3=Student('민수',70)  
students = [s1,s2,s3]
for s in students:
  print(s.name,s.score)

# %%
#5
class Score:
  def __init__(self,score):
    self.score=score
  def is_pass(self):
    if self.score>=60:
      return ('합격')
    else:
      return ('불합격')
s1=Score(65)
s2=Score(50)
print(s1.is_pass())
print(s2.is_pass())

# %%

class Cat:
  species='고양이'
  def __init__(self,name,color):
    self.name=name
    self.color=color
  def introduce(self):
    print(f'안녕 나는 {self.color}색 {Cat.species} {self.name} 고양이야')
cat1=Cat('나비','흰')
cat2=Cat('까미','검정')
cat1.introduce()
cat2.introduce()
print(Cat.species)

# %%
#6
class Student:
  school='소프트웨어고'
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def intro(self):
    print(f'{Student.school} 학생 {self.name}, {self.age}살')
s1=Student('민수',17)
s2=Student('지우',18)
s1.intro()
s2.intro()

# %%
#7
class Book:
  category='도서'
  def __init__(self,title,price):
    self.title=title
    self.price=price
  def discount(self,rate):
    self.price -= self.price * rate
  def show(self):
    print(f'{Book.category} 제목| {self.title} 가격| {self.price}원')
b=Book('파이썬 입문',20000)
b.discount(0.1)
b.show()


# %%
#8
class Character:
  game_name='RPG 게임'
  def __init__(self,name,hp):
    self.name=name
    self.hp=hp
  def attack(self,damage):
    self.hp-=damage
  def status(self):
    print(f'{self.name} HP: {self.hp} ({Character.game_name})')
c1=Character('전사',100)
c2=Character('마법사',60)
c1.attack(20)
c1.status()
c2.attack(10)
c2.status()

# %%
#9
class Student:
  school='소마고'
  def __init__(self,name,score):
    self.name=name
    self.score=score
  def intro(self):
    print(f'{Student.school} 학생 {self.name}입니다')
  def add_score(self,point):
    self.score+=point
    print(f'{self.name}의 점수가 {point}점 증가 했습니다.')
  def show_score(self):
    print(f'{self.name}의 점수는 {self.score}')
s1=Student('철수',80)
s2=Student('영희',90)
s1.intro()
s2.intro()
s1.add_score(10)
s2.add_score(5)
s1.show_score()
s2.show_score()
print('학교 :',Student.school)


