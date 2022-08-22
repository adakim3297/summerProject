from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#exception handling
from selenium.common.exceptions import NoSuchElementException
from tkinter import *
import yaml

#yaml파일에 저장된 아이디 비밀번호를 가져온다.
conf = yaml.safe_load(open('loginDetails.yml'))
myFbEmail = conf['fb_user']['email']
myFbPassword = conf['fb_user']['password']


#웹드라이버 버전에 맞도록 자동설치
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

#로그인 시도
def login(url,usernameId, username, passwordId, password, submit_buttonId):
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
def get_login_info():
   user_id = txt_id.get()
   user_pw = txt_pw.get()
   #동작부분 ( 넥슨에 로그인한다 )
   login("https://nxlogin.nexon.com/common/login.aspx?redirect=https%3A%2F%2Fwww.nexon.com%2FHome%2FGame", "txtNexonID", user_id,"txtPWD", user_pw, '//*[@id="nexonLogin"]/fieldset/div[4]/button')
   if (check_login("https://www.nexon.com/Home/Game#close",'//*[@id="contents"]/div[2]/div[4]/ul/li[1]/a')):
      #로그인 성공, 파일 작성
      f = open('tempfile.yml','w')
      f.write("fb_user:\n")
      f.write("\temail: " + user_id + "\n")
      f.write("\tpassword: " + user_pw + "\n")
      #파일 전송하기(tempfile.yml파일)
      #
      ##


root = Tk()

txt_id = Entry(root)
txt_id.grid(row=0,column=1)
txt_pw = Entry(root, show="*")
txt_pw.grid(row=1,column=1)

label_id = Label(root, text='ID:')
label_id.grid(row=0,column=0)
label_pw = Label(root, text="Password:")
label_pw.grid(row=1,column=0)

button_login = Button(root, text="login", command=get_login_info)
button_login.grid(row=2,column=1)
root.mainloop()