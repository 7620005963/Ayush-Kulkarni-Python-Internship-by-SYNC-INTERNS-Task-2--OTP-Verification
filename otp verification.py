import random
import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
password='*************'
server.login('ayushkulkarni2508@gmail.com','fmywyefwhgtdahzy')
#generate OTP using random.randint() function
otp=''.join([str(random.randint(0,9)) for i in range(4)])
msg='Hello, Your OTP is '+str(otp)
sender='ayushkulkarni2508@gmail.com'
receiver='ayushkulkarni2508@gmail.com'
server.sendmail('ayushkulkarni2508@gmail.com','ayushkulkarni2508@gmail.com',msg)
server.quit()
