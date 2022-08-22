# SMTP를 이용한 이메일 전송

## 1. SMTP를 이용해서 user가 입력한 정보를 원하는 이메일로 전송한다.

### <SMTP란?>
    인터넷에서 메일을 주고 받기 위한 전송규약 및 프로토콜

    SMTP 서버란?
    * 중계전달자 역할
    * SMTP 프로토콜을 사용해 이메일을 전송하고 수신할 수 있는 메일 서버 즉, 메일 서버 간의 송수신, 메일 클라이언트에서 서버로 보낼 때 사용되는 프로토콜 

참고 자료 : https://mutpp.tistory.com/4

    * SMTP에서 사용하는 포트(네트워크 데이터 수신하는 가상 지점)는?

        * 포트 587 :  이메일 제출용 기본 포트
        이 포트를 통과하는 SMTP 통신 >>> TLS 암호화를 이용


## 2. Gmail에서 IMAP을 이용한다.
### <IMAP이란?>
* Internet Message Access Protocol
    

    Python에서 smtplib모듈을 사용해서 SMPT서버를 사용할 수 있는 Google 설정에서 IMAP을 허용하여 메일을 보냄


### IMAP와 POP

* 인터넷 메시지 접속 프로토콜(IMAP)과 포스트 오피스 프로토콜(POP)은 최종 수신처로 이메일을 전달

* 사용자에게 이메일을 표시하려면 이메일 클라이언트가 망 내 최종 메일 서버에서 이메일을 검색

## 3. SMTP (Python) 

    import smtplib, os
    from email import encoders
    import smtplib, os
    from email import encoders
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
   
    *  encoders : 텍스트 외에 file을 문자열로 변환해서 보내기 위해 사용하는 모듈
    * MIMEText : 메일 보낼때 메세지 제목, 본문
    * MIMEMultipart : 메세지 보낼때의 메세지에 대한 모듈
    * MIMEBase : 전송할때 사용하는 모듈