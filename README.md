# 빅데이터를 위한 Python

## 네이버 API key 발급
1. .env_copy 를 .env 로 복사
2. 네이버 개발자 센터로 로그인
3. 서비스 API 클릭
4. open api 이용 신청 클릭
5. 약관 동의
6. 이메일 확인 (회사이름은 공백으로)
7. 애플리케이션 등록(API 이용신청) 화면에서
    * 애플리케이션 이름 : api_20260112
    * 사용 API : 검색
    * 환경추가 : 웹설정
    * 비로그인 오픈API 서비스 환경 : http://naver.com
8. Client ID 와 Client Secret 의 값을 .env파일에 적어 놓는다

## 파이썬에서 .env 파일 내용 읽기
1. uv add python-dotenv
2. 파이썬에서 .env 내용을 읽을려면 아래 내용을 추가한다
    * import os
    * from dotenv import load_dotenv
    * load_dotenv()
    * client_id = os.getenv("Client_ID")
    * client_secret = os.getenv("Client_Secret")