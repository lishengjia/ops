#coding:utf-8
from modules.users.mysql_opertation import UserSqlOperation
from modules.machines.mysql_opertation import AllMachineInfo


class Check():
    def __init__(self):
        pass

    @staticmethod
    def md5(result):
        import hashlib
        m = hashlib.md5()
        m.update(result)
        return m.hexdigest()

    @staticmethod
    def host_check(result, flag):
        check_ip = AllMachineInfo.add_host_check(result["server_ip"])
        str_check_empty = "<script language='javascript'>alert('内网地址必须填写');window.history.back(-1);</script>"
        str_check_existed = "<script language='javascript'>alert('内网地址已经存在');window.history.back(-1);</script>"
        if result["server_ip"] == '':
            return str_check_empty
        elif flag:
            if check_ip:
                if result["server_ip"] == check_ip[0][0]:
                    return str_check_existed
            else:
                return "ok"
        else:
            return "ok"

    @staticmethod
    def login_check(input_username, input_password):
        mysql_user_password = UserSqlOperation.check_user_login(input_username)
        if mysql_user_password:
            md5_input_password = Check.md5(input_password)
            if mysql_user_password[0][1] == md5_input_password:
                return "ok"
            else:
                return "Incorrect password"
        else:
            return "Invalid username"

    @staticmethod
    def user_modify_check(result, flag):
        str_check_empty = "<script language='javascript'>alert('用户名或密码不能为空');window.history.back(-1);</script>"
        str_check_existed = "<script language='javascript'>alert('用户名已经存在');window.history.back(-1);</script>"
        str_check_length = "<script language='javascript'>alert('密码长度大于20位');window.history.back(-1);</script>"
        if result["user_name"] == "" or result["user_password"] == "":
            return str_check_empty
        elif len(result["user_password"]) == 32:
            return "md5"
        elif len(result["user_password"]) >= 20:
            return str_check_length
        elif len(result["user_password"]) < 20:
            if flag:
                check_username = UserSqlOperation.user_modify_check(result["user_name"])
                print check_username
                if check_username:
                    if check_username[0][0] == result["user_name"]:
                        return str_check_existed
                else:
                    return "ok"
            else:
                return "ok"