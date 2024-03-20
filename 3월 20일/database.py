import pymysql

class myDB:
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
        mydb = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.pw,
            db = self.db
        )
        cursor = mydb.cursor(pymysql.cursors.DictCursor)
        cursor.execute(_sql, _values)
        if _sql.lower().strip().startswith('select'):
            result = cursor.fetchall()
        else:
            mydb.commit()
            result = 'Commit Succesfully'
        mydb.close()
        return result