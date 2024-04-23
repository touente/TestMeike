from utils.mysql_util import db


class DbOperate:
    def get_goods_ids(self):
        sql = "SELECT id FROM goods_goods"
        result = db.select_db_all(sql)
        return result

    def get_user_id(self, mobile):
        sql = "SELECT id FROM users_userprofile WHERE mobile = '%s'" % mobile
        result = db.select_db_one(sql)
        return result

    def get_goods_num(self, mobile, goods_id):
        user_id = self.get_user_id(mobile)
        sql = "SELECT nums FROM trade_shoppingcart WHERE user_id = %s AND goods_id = %s" % (user_id, goods_id)
        result = db.select_db_one(sql)
        return result

    def get_user_goods(self, user_id):
        sql = "select goods_id from trade_shoppingcart where user_id = %s" % user_id
        result = db.select_db_all(sql)
        return result


dbo = DbOperate()
