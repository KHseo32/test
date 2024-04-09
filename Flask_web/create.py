## 데이터베이스에 테이블을 생성하는 쿼리문들을 모아서 저장
import database

# 서버에 정보를 입력 (Class 생성)
_db = database.MyDB1()

## 게시판 테이블을 생성하는 쿼리문 작성
board_create = """
    CREATE TABLE
    IF NOT EXISTS
    `board`(
        No int primary key auto_increment,
        title text not null,
        writer varchar(32) not null,
        create_dt varchar(64) not null,
        content text
    )
"""
result = _db.sql_query(board_create)
print(result)