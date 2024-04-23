import pymysql
from utils.log_util import logger
from utils.read_util import base_data

data = base_data.read_ini()['mysql']
DB_CONF = {
    "host": data['MYSQL_HOST'],
    "port": int(data['MYSQL_PORT']),
    "user": data['MYSQL_USER'],
    "password": data['MYSQL_PASSWD'],
    "db": data['MYSQL_DB'],
}


class MysqlDb:
    # MySQL链接
    def __init__(self):
        self.conn = pymysql.connect(**DB_CONF, autocommit=True)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 释放资源
    def __del__(self):
        self.cur.close()
        self.conn.close()

    # 只返回查询结果的值，不返回字典
    def select_db_one(self, sql):
        logger.info(f'执行sql：{sql}')
        self.cur.execute(sql)
        result = self.cur.fetchone()
        logger.info(f'sql执行结果：{result}')
        if result is not None:
            result2 = list(result.values())[0]
        else:
            result2 = 0
        return result2

    # 返回字典
    def select_db_all(self, sql):
        logger.info(f'执行sql：{sql}')
        self.cur.execute(sql)
        result = self.cur.fetchall()
        logger.info(f'sql执行结果：{result}')
        if result is None:
            result = 0
        return result

    def execute_db(self, sql):
        try:
            logger.info(f'执行sql：{sql}')
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logger.info("执行sql语句出错{}", format(e))


db = MysqlDb()


