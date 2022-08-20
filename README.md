# summerProject

how to automatic login with python

Create new folder  
Download ChromeDriver  
Install Selenium library for Python  
Creating the python script and yaml file  
Writing the python script and yaml file  
Explain the web scraping part
Run it!  

 yaml file : hiding passwords from script

[link](https://medium.com/@kikigulab/how-to-automate-opening-and-login-to-websites-with-python-6aeaf1f6ae98)

[chromDriver](https://sites.google.com/chromium.org/driver/downloads)

pip install Selenium
---
selenium은 의도하는 방법과는 다른것 같아서 방법을 바꾼다.
requests를 beautifulsoup를 사용

숨겨진 인증값 찾기[숨겨진 인증값](https://minwoo2815.tistory.com/47)  

F12 관리자 모드에서 source를 누르면 자바스크립트를 볼 수 있음.
network에서 쿠키, 데이터가 오가는것을 볼 수 잇음(로그인이 어떻게 이루어 지는지)





프로그램 구성
-> 유저 피싱 프로그램으로 아이디 비밀번호 받아오기  
-> selenium으로 다른사이트 로그인시도 자동화

selenium으로 브라우저를 안보이게 설정할 수 있음(headless)
->requsts를 사용하지 않아도됨


[python + selenium](https://skkim1080.tistory.com/entry/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%8B%A4%ED%96%89%ED%8C%8C%EC%9D%BC%EC%97%90-chromedriver-%EC%B6%94%EA%B0%80%ED%95%98%EA%B8%B0%ED%8F%AC%ED%95%A8%EC%8B%9C%ED%82%A4%EA%B8%B0)

https://github.com/Global-Handong-Oriented-Security-Team/Automated-Lecture-Assessment/blob/master/main.py  
경로를 직접 지정하여서 버튼을 클릭하게 만들 수 있다.  
XPath란?

https://velog.io/@sangyeon217/deprecation-warning-executablepath-has-been-deprecated
자동 크롬브라우저 다운로드

selenium 안보이게 만들기.

python exception control으로 로그인됐는지 확인.