## 기본적인 웹서버 설정
## flask 웹프레임워크를 로드
from flask import Flask, render_template, request, redirect
## module 로드
import database


## Flask라는 Class 생성
## 생성자 함수 필수 인자 : 파일의 이름(app.py)
## __name__ : 현재 파일의 이름
app = Flask(__name__)

## 주소 생성(api 생성)
## localhost : 5000/ 요청시 index 함수 호출
@app.route('/')
def index():
    # 문자열을 return 하는 것이 아니라 html 문서를 리턴
    # return "Hello World"
    # render_template : templates 폴더 안에 있는 html
    return render_template('index.html')

## 주소 생성
## localhost : 5000/second
@app.route('/second')
def second():
    # return 'Second Page'
    return render_template('login.html')

## login 주소 생성
## 로그인 정보(request 메시지)를 받아오는 주소
@app.route('/login')
def login():
    # 해당 주소로 요청이 들어왔을 때(유저가 보낸 데이터가 포함)
    ## request.args : 유저가 서버에게 get 방식으로 보낸 데이터가 저장되어 있는 공간
    req = request.args
    print(req)
    # 유저가 보낸 아이디와 비밀번호 변수에 저장
    _id = req['input_id']
    _password = req['input_password']
    print(f'유저가 보낸 아이디 : {_id}   비밀번호 : {_password}')
    ## _id가 test이고 _password가 1111인 경우 로그인 성공 메세지 리턴
    if(_id == 'test') & (_password == '1111'):
        return "로그인 성공"
    ## 실패한 경우 로그인 페이지(/second)로 되돌아간다.
    else :
        return redirect('/second')


## Flask Class 안에 있는 (웹서버 구동)함수 호출
app.run(debug=True)