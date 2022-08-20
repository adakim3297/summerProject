from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#exception handling
from selenium.common.exceptions import NoSuchElementException
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
   except NoSuchElementException:
      #로그인 실패
      print("로그인 실패")

#동작부분 ( 넥슨에 로그인한다 )
login("https://nxlogin.nexon.com/common/login.aspx?redirect=https%3A%2F%2Fwww.nexon.com%2FHome%2FGame", "txtNexonID", myFbEmail,"txtPWD", myFbPassword, '//*[@id="nexonLogin"]/fieldset/div[4]/button')
check_login("https://www.nexon.com/Home/Game#close",'//*[@id="contents"]/div[2]/div[4]/ul/li[1]/a')