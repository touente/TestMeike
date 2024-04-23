from utils.mysql_util import db


class DbOperate:
    def get_bd_code(self, mobile):
        sql = "SELECT users_verifycode.code FROM users_verifycode WHERE users_verifycode.mobile = '%s' ORDER BY users_verifycode.add_time DESC" % mobile
        result = db.select_db_one(sql)
        return result

    def get_db_user(self, mobile):
        sql = "SELECT users_userprofile.id FROM users_userprofile WHERE users_userprofile.mobile = '%s'" % mobile
        result = db.select_db_one(sql)
        return result

    def delete_db_user(self, mobile):
        sql = "DELETE FROM users_userprofile WHERE users_userprofile.mobile = '%s'" % mobile
        db.select_db_all(sql)


dbo = DbOperate()
