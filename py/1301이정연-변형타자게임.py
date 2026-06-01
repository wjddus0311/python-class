import random, time
b=input('동물을 추가하시겠습니까? (y/n)')#리스트에 동물을 추가 할것인지 물어봄
if b=='y':
    a=input('추가할 동물을 입력하세요.(영어로)') #리스트에 추가할 동물을 입력받음
else:
    pass
w =['cat','dog','fox','monkey','mouse','panda','frog','snake','wolf','pig']
w.append(a) #리스트 w에 추가
n=0
h=0
print('준비되면 엔터')
start = time.time()
for i in range(5):
    wo=random.choice(w)
    print('단어',wo)
    us=input('입력:')
    if us==wo:
        print('정답')
        n+=1

        h+=10 #정답일때마다 10점씩 추가
    else:
        print('오답')
        h-=3 #오답일때마다 -3점
end= time.time()
if h>=30:
    print('당신은 타자의 신입니다')
print('\n 총 맞춘 갯수',n)
print("\n총 걸린 시간:", round(end - start, 2), "초")
print('\n 총점',h) #총 점수 출력

#타자연습을 하고 싶은 동물 이름을 입력받아서 리스트에 추가한 후 타자연습을 시작함.
#문제를 맞출때마다 +10점 틀릴때마다 -3점
#타자연습을 다하고 총점이 30점 이상인 경우에 타자의 신이라는 문구가 출력된다.
    