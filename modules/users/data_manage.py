#coding:utf-8

"""data manage"""


class UserDataManage(object):
    @staticmethod
    def manage_user_list(result):
        dict_data = {}
        for line in result:
            tmp_dict = dict()
            tmp_dict["user_name"] = line[1]
            tmp_dict["user_password"] = line[2]
            tmp_dict["role_name"] = line[3]
            dict_data[line[0]] = tmp_dict
        return dict_data