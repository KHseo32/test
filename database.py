import pymysql

class MyDB1:
    def __init__(
            self,
            _host = 'localhost',
            _port = 3306,
            _user = 'root',
            _pw = '1234',
            _db = 'ubion'
    ):
        self.host = _host
        self.port = _port
        self.user = _user
        self.pw = _pw
        self.db = _db
    def sql_query(self, _sql, *_values):
        MyDB1 = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.pw,
            db = self.db
        )
        cursor = MyDB1.cursor(pymysql.cursors.DictCursor)
        cursor.execute(_sql, _values)
        if _sql.lower().strip().startswith('select'):
            result = cursor.fetchall()
        else:
            MyDB1.commit()
            result = 'Commit Succesfully'
        MyDB1.close()
        return result