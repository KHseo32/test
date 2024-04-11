# 프레임 워크 로드
from flask import Flask, request
import pandas as pd
import database 
# Flask Class 생성
# __name__ : 현재 파일의 이름
app = Flask(__name__)


_db = database.MyDB1(
    _host = '172.30.1.22',
    _user = 'ubion',
    _pw = '1234',
    _database = 'ubion'
)
# api 생성

@app.route('/')
def index():
    try:
        _id = request.args['input_id']
        _pass = request.args['input_pass']
    except:
        return 'parameter error'
    print(_id, _pass)
    query = """
    SELECT * FROM user WHERE id = %s AND password = %s
    """
    result = _db.sql_query(query, _id, _pass)
    if result:
        # 외부의 csv 파일을 로드
        df = pd.read_csv('./corona.csv', index_col= 0)
        data = df.to_dict()
        return data
    else:
        return '입력 데이터 오류'


##웹서버 실행
app.run(debug=True)