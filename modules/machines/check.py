#coding:utf-8
from modules.machines.mysql_opertation import AllMachineInfo


class Check():
    def __init__(self):
        pass

    @staticmethod
    def host_check(result, flag):
        check_ip = AllMachineInfo.add_host_check(result["server_ip"])
        str_check_empty = "<script language='javascript'>alert('内网地址必须填写');window.history.back(-1);</script>"
        str_check_existed = "<script language='javascript'>alert('内网地址已经存在');window.history.back(-1);</script>"
        if flag:
            if result["server_ip"] == '':
                return str_check_empty
            elif check_ip:
                if result["server_ip"] == check_ip[0][0]:
                    return str_check_existed
            else:
                return "ok"
        else:
            if result["server_ip"] == '':
                return str_check_empty
            else:
                return "ok"