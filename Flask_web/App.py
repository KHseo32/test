## 기본적인 웹서버 설정
## flask 웹프레임워크를 로드
from flask import Flask, render_template, request, redirect, url_for
## module 로드
import database


## Flask라는 Class 생성
## 생성자 함수 필수 인자 : 파일의 이름(app.py)
## __name__ : 현재 파일의 이름
app = Flask(__name__)
## database에 있는 MYDB1 Class 생성
_db = database.MyDB1(
    _host = '172.30.1.55',
    _user = 'ubion',
    _pw = '1234',
    _db = 'ubion'
)
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
    _pw = req['input_password']
    print(f'유저가 보낸 아이디 : {_id}   비밀번호 : {_pw}')
    ## _id가 test이고 _password가 1111인 경우 로그인 성공 메세지 리턴
    # if(_id == 'test') & (_password == '1111'):
    #     return "로그인 성공"
    ## 실패한 경우 로그인 페이지(/second)로 되돌아간다.
    # else :
    #     return redirect('/second')
    ## 유저가 보낸 데이터를 DB server의 정보와 비교
    query = """
        SELECT * FROM `user` WHERE `id` = %s AND `password` = %s
    """
# _db 안에 있는 sql_query() 함수를 호출
    result = _db.sql_query(query, _id, _pw)
    print(result)
# 로그인이 성공하는 조건 : result 데이터가 존재할 때
    if result:
        return "로그인 성공"
    else:
        return redirect('/second')

# 127.0.0.1 : 5000/login2 [post] 주소 생성
@app.route('/login2', methods=['post'])
def login2():
    # get 방식으로 데이터를 보내는 경우 -> request.args
    # post 방식으로 데이터를 보내는 경우 -> request.form
    req = request.form
    print('post 방식 데이터 :', req)
    _id = req['input_id']
    _pw = req['input_password']
    print(f'유저가 보낸 아이디 : {_id}  비밀번호 : {_pw}')
    query = """
        SELECT * FROM `user` WHERE `id` = %s AND `password` = %s
    """
    result = _db.sql_query(query, _id, _pw)
    if result:
        # return "로그인 성공"
        # 로그인 성공시 main.html을 되돌려준다.
        # 로그인 정보 중 유저의 이름을 변수에 저장
        user_name = result[0]['name']
        print("로그인을 한 유저의 이름 : ", user_name)
        return render_template('main.html', _name = user_name)
    else:
        return redirect('/second')

# 회원가입 화면을 보여주는 주소를 생성
@app.route('/signup')
def signup():
    return render_template('signup.html')
# 회원의 정보를 받아오는 주소를 생성 
# 127.0.0.1:5000/signup2 [post]
@app.route('/signup2', methods=['post'])
def signup2():
    # 유저가 보낸 정보를 확인 -> 변수에 저장
    # 유저가 보낸 정보 -> request안에 데이터의 형태는 dict로 구성
    # {key(input태그에 있는 name 속성의 값) : value(input태그에 유저가 입력한 데이터)}
    # post 방식으로 데이터를 보내면 request안에 form에 데이터가 존재
    req = request.form
    print("회원가입 데이터 : ", dict(req))
    _id = req['input_id']
    _pw = req['input_password']
    _name = req['input_name']
    print('회원 ID', _id, '비밀번호', _pw, '이름', _name)
    # 받아온 회원 정보를 DB 에 INSERT문을 실행
    query = """
        INSERT INTO 
        `user`
        VALUES (%s, %s, %s)
    """
    try:
        result = _db.sql_query(query, _id, _pw, _name)
        print(result)
        # 회원 가입이 완료되었으면
        return redirect('/second')
    except:
        return 'ID 중복'


## Flask Class 안에 있는 (웹서버 구동)함수 호출
app.run(debug=True)