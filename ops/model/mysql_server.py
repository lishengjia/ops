#coding: utf-8

""" Mysql数据库操作 """

import MySQLdb
import logging

logger = logging.getLogger(__name__)


class MysqlServer(object):
    """连接Mysql数据服务器 """

    def __init__(self, db_config):
        try:
            self._db_config = db_config
            self._conn = self.__get_conn()
            self._cursor = self._conn.cursor()
            logger.info(u"创建数据库连接")
        except Exception:
            self.close()
            logger.exception(u"数据库连接失败!")

    def __get_conn(self):
        db_config = self._db_config
        connection = MySQLdb.connect(host=db_config['HOST'], port=db_config['PORT'], user=db_config['USERNAME'],
                                     passwd=db_config['PASSWORD'], db=db_config['DB'], charset="utf8")
        return connection

    def ensure_cursor(self):
        if not self._cursor:
            if not self._conn:
                self._conn = self.__get_conn()
            self._cursor = self._conn.cursor()

    def run_sql(self, sql):
        self.ensure_cursor()
        self._cursor.execute(sql)
        #commit只对innodb生效，不加commit的话，修改数据库记录的操作不会生效。而如果是myisam引擎的话，不需要commit即可生效
        self._conn.commit()
        return self._cursor.fetchall()

    def execute_sql(self, sql):
        self.ensure_cursor()
        self._cursor.execute(sql)
        self._conn.commit()

    def run_sql_fetchone(self, sql):
        self.ensure_cursor()
        self._cursor.execute(sql)
        return self._cursor.fetchone()

    def close(self):
        if self._cursor:
            self._cursor.close()
        if self._conn:
            self._conn.close()

        logger.info(u"关闭数据库连接")
