# %%



class Notification:
  def __init__(self,user):
    self.user=user
  def send(self,message):
    self.message=message
    print(f'{self.user}에게 알림:{message}')
  def get_user(self):
    return self.user
class EmailNotification(Notification):
  def send(self,message):
    self.message=message
    print(f'[이메일]{self.user}에게 알림:{message}')
class SMSNotification(Notification):
  def send(self,message):
    self.message=message
    print(f'[문자]{self.user}에게 알림:{message}')
class AppNotification(Notification):
  def send(self,message):
    self.message=message
    print(f'[앱푸시]{self.user}에게 알림:{message}')

email=EmailNotification('철수')
sms=SMSNotification('영희')
app=AppNotification('민수')
email.send('회원가입 완료')
sms.send('인증번호 1234')
app.send('새 메시지가 도착했습니다.')
print(f'사용자 이름:{email.user}')
print(f'사용자 확인:{sms.get_user()}')
notice=[email,sms,app]
for i in notice:
  i.send('회원가입을 축하합니다')

# %%

class Notification:
  platform='공통 알림 시스템'
  def __init__(self,user):
    self.user=user
  def send(self,message):
    self.message=message
    print(f'{self.user}에게 알림:{message}')
class EmailNotification(Notification):
  method='이메일'
  def send(self,message):
    self.message=message
    print(f'[이메일]{self.user}에게 전송:{message}')
class SMSNotification(Notification):
  method='문자'
  def send(self,message):
    self.message=message
    print(f'[문자]{self.user}에게 전송:{message}')
class AppNotification(Notification):
  method='앱푸시'
  def send(self,message):
    self.message=message
    print(f'[앱푸시]{self.user}에게 전송:{message}')
#15
class KakaoNotification(Notification):
  method='카카오톡'
  def send(self,message):
    self.message=message
    print(f'[카카오톡]{self.user}에게 전송:{message}')

#1
email=EmailNotification('철수')
sms=SMSNotification('영희')
app=AppNotification('민수')
kakao=KakaoNotification('수진')

#2
print(email.user)
print(sms.user)
print(app.user)

#3
print(Notification.platform)

#4
print(email.platform) 
print(sms.platform)   
print(app.platform)

#5
print(EmailNotification.method)
print(SMSNotification.method)
print(AppNotification.method)
#6
print(email.method)
print(sms.method)
print(app.method)
#7
email.send('비밀번호 변경 완료')
sms.send('인증번호 1234')
app.send('새 메시지가 도착했습니다.')
kakao.send('친구 요청이 도착했습니다')
#8
noti=Notification('관리자')
noti.send('시스템점검안내')
#9
email=EmailNotification('지민')
email.send('비밀번호 변경 완료')
#10
list=[email,sms,app]
for i in list:
  i.send('공지사항이 있습니다')
#12
print(type(email))
print(type(sms))
print(type(app))
#13
print(isinstance(email,EmailNotification))
print(isinstance(email,Notification))
#14
print(isinstance(noti,Notification))
print(isinstance(noti,EmailNotification))
#17
Notification.platform='학교 알림 시스템'
print(email.platform)
print(sms.platform)
print(app.platform)
#18
email.title='가입안내'
print(email.title)
#19
#email.cancel()



# %%
#20
class Notification:
  platform='공통 알림 시스템'
  def __init__(self,user):
    self.user=user
  def send(self,message):
    self.message=message
    print(f'{self.user}에게 알림:{message}')
class EmailNotification(Notification):
  method='이메일'
  def send(self,message):
    self.message=message
    print(f'[이메일]{self.user}에게 전송:{message}')
class SMSNotification(Notification):
  method='문자'
  def send(self,message):
    self.message=message
    print(f'[문자]{self.user}에게 전송:{message}')
class AppNotification(Notification):
  method='앱푸시'
  def send(self,message):
    self.message=message
    print(f'[앱푸시]{self.user}에게 전송:{message}')

email=EmailNotification('철수')
sms=SMSNotification('영희')
app=AppNotification('민수')




print(email.user)
print(email.method)
print(email.platform)
email.send('오늘 수업이 있습니다')
print(sms.user)
print(sms.method)
print(sms.platform)
sms.send('오늘 수업이 있습니다')
print(app.user)
print(app.method)
print(app.platform)
app.send('오늘 수업이 있습니다')




