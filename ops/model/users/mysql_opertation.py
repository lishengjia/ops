#coding:utf-8

""" 执行mysql语句 """
from ops import settings
from ops.model.mysql_server import MysqlServer


class UserSqlOperation(object):
    @staticmethod
    def check_user_login(result):
        db = MysqlServer(settings.DATABASES)
        sql = "select `username`,`userpassword` from zc_user where username='%s'" % result
        result = db.run_sql(sql)
        db.close()
        return result

    @property
    def user_list(self):
        db = MysqlServer(settings.DATABASES)
        sql = "select `uid`,`username`,`userpassword`,`rolename` from zc_user left join zc_role on \
        zc_user.rid = zc_role.id"
        result = db.run_sql(sql)
        db.close()
        return result

    @staticmethod
    def user_delete(result):
        db = MysqlServer(settings.DATABASES)
        sql = "delete from zc_user where uid='%d'" % int(result)
        db.execute_sql(sql)
        db.close()

    @staticmethod
    def user_modify(result):
        db = MysqlServer(settings.DATABASES)
        sql = "select `uid`,`username`,`userpassword`,`rolename` from zc_user left join zc_role on \
        zc_user.rid = zc_role.id where uid='%d'" % int(result)
        result = db.run_sql(sql)
        db.close()
        return result

    @staticmethod
    def user_modify_update(result, uid):
        db = MysqlServer(settings.DATABASES)
        sql = "update zc_user set username='%s',userpassword='%s' where uid='%s'" % (result["user_name"],
        result["user_password"], uid)
        print sql
        db.execute_sql(sql)
        db.close()

    @staticmethod
    def user_modify_check(result):
        db = MysqlServer(settings.DATABASES)
        sql = "select `username` from zc_user where username='%s'" % result
        result = db.run_sql(sql)
        db.close()
        return result

    @staticmethod
    def add_user(result):
        db = MysqlServer(settings.DATABASES)
        sql = '''insert into zc_user (rid,username,userpassword) values ("%d","%s","%s")''' % (1, str(result["user_name"]), str(result["user_password"]))
        print sql
        db.execute_sql(sql)
        db.close()