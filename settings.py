#coding:utf-8


template_variables = dict(
    title=u'OPS',
    name=u'OPS管理平台',
    login_username="",
)

DATABASES = dict(
    DB='ops',
    USERNAME='root',
    PASSWORD='123456',
    HOST='127.0.0.1',
    PORT=3306,
)

ADD_HOST_LIST = ["server_ip", "public_ip", "idc_name", "mem_size", "disk_size", "cpu_num",
                 "server_rack", "sn", "server_type", "os", "project_name", "server_status", "server_contact", "comment"]

cookie_name = "user_id"