#coding:utf-8

""" 执行mysql语句 """
import settings
from modules.mysql_server import MysqlServer


class AllMachineInfo(object):
    @property
    def machine_list(self):
        db = MysqlServer(settings.DATABASES)
        sql = "select `serverip`,`publicip`,`idcname`,`memsize`,`cpunum`,`disksize`,`serverrack`,`sn`, \
        `stype`,`os`,`sname`,`mstatus`,`cname`,`cinfo`,`comment`,zc_machine.`mid` from zc_machine left join zc_idc on zc_machine.rid = zc_idc.rid \
        left join zc_service on zc_machine.service = zc_service.sid left join zc_contact on \
        zc_machine.ccid = zc_contact.ccid"
        result = db.run_sql(sql)
        db.close()
        return result

    @property
    def add_host_select(self):
        db = MysqlServer(settings.DATABASES)
        sql_idc = "select `rid`,`idcname` from zc_idc"
        sql_project = "select `sid`,`sname` from zc_service"
        sql_contact = "select `ccid`,`cname` from zc_contact"
        sql_status = "select `mstatus` from zc_machine group by `mstatus`"
        result_idc = db.run_sql(sql_idc)
        result_project = db.run_sql(sql_project)
        result_contact = db.run_sql(sql_contact)
        result_status = db.run_sql(sql_status)
        db.close()
        return result_idc, result_project, result_contact, result_status

    @staticmethod
    def add_host_check(result):
        db = MysqlServer(settings.DATABASES)
        sql = "select `serverip` from zc_machine where serverip='%s'" % result
        result = db.run_sql(sql)
        db.close()
        return result

    @staticmethod
    def add_host(result):
        db = MysqlServer(settings.DATABASES)
        sql = "insert into zc_machine (serverip, publicip , rid, memsize, cpunum, disksize, \
        serverrack, sn, stype, os, service, mstatus, ccid, comment) \
        values ('%s', '%s', '%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%d', '%s', '%d', '%s')" % \
        (result["server_ip"], result["public_ip"], int(result["idc_name"]), result["mem_size"],
         result["cpu_num"], result["disk_size"], result["server_rack"], result["sn"],
         result["server_type"], result["os"], int(result["project_name"]), result["server_status"],
         int(result["server_contact"]), result['comment'])
        db.execute_sql(sql)
        db.close()

    @staticmethod
    def modify_host(result):
        db = MysqlServer(settings.DATABASES)
        sql = "select `serverip`,`publicip`,`idcname`,`memsize`,`cpunum`,`disksize`,`serverrack`,`sn`, \
        `stype`,`os`,`sname`,`mstatus`,`cname`,`cinfo`,`comment`,zc_machine.`mid` from zc_machine left join zc_idc on zc_machine.rid = zc_idc.rid \
        left join zc_service on zc_machine.service = zc_service.sid left join zc_contact on \
        zc_machine.ccid = zc_contact.ccid where mid='%s'" % result
        result = db.run_sql(sql)
        db.close()
        return result

    @staticmethod
    def modify_host_update(result, mid):
        db = MysqlServer(settings.DATABASES)
        sql = "update zc_machine set serverip='%s', publicip='%s', rid='%d', memsize='%s', cpunum='%s', \
         disksize='%s', serverrack='%s', sn='%s', stype='%s', os='%s', service='%d', mstatus='%s', ccid='%d', \
          comment='%s' where mid='%d' " % \
        (result["server_ip"], result["public_ip"], int(result["idc_name"]), result["mem_size"],
         result["cpu_num"], result["disk_size"], result["server_rack"], result["sn"],
         result["server_type"], result["os"], int(result["project_name"]), result["server_status"],
         int(result["server_contact"]), result['comment'], int(mid))
        db.execute_sql(sql)
        db.close()

    @staticmethod
    def delete_host(result):
        db = MysqlServer(settings.DATABASES)
        sql = "delete from zc_machine where mid='%d'" % int(result)
        db.execute_sql(sql)
        db.close()

    @staticmethod
    def search_hosts(result):
        db = MysqlServer(settings.DATABASES)
        sql = "select `serverip`,`publicip`,`idcname`,`memsize`,`cpunum`,`disksize`,`serverrack`,`sn`, \
        `stype`,`os`,`sname`,`mstatus`,`cname`,`cinfo`,`comment`,zc_machine.`mid` from zc_machine left join \
        zc_idc on zc_machine.rid = zc_idc.rid left join zc_service on zc_machine.service = zc_service.sid \
        left join zc_contact on zc_machine.ccid = zc_contact.ccid where serverip like '%%%s%%' and publicip like \
        '%%%s%%' and idcname like '%%%s%%' and memsize like '%%%s%%' and cpunum \
        like '%%%s%%' and disksize like '%%%s%%' and serverrack like '%%%s%%' and sn like '%%%s%%' and stype like \
        '%%%s%%' and os like '%%%s%%' and sname like '%%%s%%' and mstatus like '%%%s%%' and cname like '%%%s%%' and \
        comment like '%%%s%%'" % (result["server_ip"], result["public_ip"], result["idc_name"], result["mem_size"],
        result["cpu_num"], result["disk_size"], result["server_rack"], result["sn"], result["server_type"], result["os"],
        result["project_name"], result["server_status"], result["server_contact"], result['comment'])
        result = db.run_sql(sql)
        db.close()
        return result

    @staticmethod
    def search_hosts_quick(result):
        db = MysqlServer(settings.DATABASES)
        sql = "select `serverip`,`publicip`,`idcname`,`memsize`,`cpunum`,`disksize`,`serverrack`,`sn`, \
        `stype`,`os`,`sname`,`mstatus`,`cname`,`cinfo`,`comment`,zc_machine.`mid` from zc_machine left join \
        zc_idc on zc_machine.rid = zc_idc.rid left join zc_service on zc_machine.service = zc_service.sid \
        left join zc_contact on zc_machine.ccid = zc_contact.ccid where serverip like '%%%s%%'" % result
        result = db.run_sql(sql)
        db.close()
        return result
