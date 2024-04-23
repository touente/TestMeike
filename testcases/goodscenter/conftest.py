from utils.mysql_util import db


class DbOperate:
    def get_banner_count(self):
        sql = "SELECT count(*) FROM goods_banner"
        result = db.select_db_one(sql)
        return result


dbo = DbOperate()



