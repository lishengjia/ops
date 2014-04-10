#coding:utf-8
import time

import tornado.web

from modules.base import BaseHandler
import settings
from modules.machines.mysql_opertation import AllMachineInfo
from modules.machines.data_manage import DataManage
from modules.check import Check


class MachineList(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        server_data = AllMachineInfo().machine_list
        server_data_handled = DataManage.manage_machine_list(server_data)
        server_length = len(server_data_handled)
        page = self.get_argument("page", default="1")
        self.render('machines/main.html', name=settings.template_variables, server_data=server_data_handled,
                    server_length=server_length, page=int(page))


class AddHost(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        select_data = AllMachineInfo().add_host_select
        select_data_handled, status_handled = DataManage.manage_add_host_select(select_data)
        self.render('machines/add_host.html', name=settings.template_variables, select_data=select_data_handled,
                    select_data_status=status_handled)

    def post(self, *args, **kwargs):
        data_dic = dict()
        data_list = settings.ADD_HOST_LIST
        for name in data_list:
            data_dic[name] = self.get_argument(name)
        server_select = self.get_argument("server_select_status")
        if data_dic["server_status"].strip() == '':
            data_dic["server_status"] = server_select
        result = Check.host_check(data_dic, True)
        if result == "ok":
            data_dic["create_time"] = time.strftime('%Y-%m-%d %H:%M:%S')
            AllMachineInfo.add_host(data_dic)
            self.write("<script language='javascript'>alert('添加完成');window.location.href='/addhost';</script>")
        else:
            self.write(result)


class ModifyHost(BaseHandler):
    machine_id = ""

    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        action = self.get_argument('action')
        ModifyHost.machine_id = self.get_argument('mid')
        if action == 'modify':
            host_data = AllMachineInfo.modify_host(ModifyHost.machine_id)
            host_data_handled = DataManage.manage_machine_list(host_data)
            select_data = AllMachineInfo().add_host_select
            select_data_handled, status_handled = DataManage.manage_add_host_select(select_data)
            self.render('machines/modify_host.html', name=settings.template_variables, select_data=select_data_handled,
                        select_data_status=status_handled, host_data=host_data_handled)
        elif action == 'delete':
            AllMachineInfo.delete_host(ModifyHost.machine_id)
            page = self.get_argument("page")
            js_str = "<script language='javascript'>window.location.href='/?page=%s';</script>" % page
            self.write(js_str)

    def post(self, *args, **kwargs):
        data_dic = dict()
        data_list = settings.ADD_HOST_LIST
        for name in data_list:
            data_dic[name] = self.get_argument(name)
        server_select = self.get_argument("server_select_status")
        if data_dic["server_status"].strip() == '':
            data_dic["server_status"] = server_select
        result = Check.host_check(data_dic, False)
        if result == "ok":
            data_dic["modify_time"] = time.strftime('%Y-%m-%d %H:%M:%S')
            AllMachineInfo.modify_host_update(data_dic, ModifyHost.machine_id)
            self.write("<script language='javascript'>alert('修改完成');window.location.href='/';</script>")
        else:
            self.write(result)


class SearchHosts(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        if self.get_argument('search') == 'server_ip':
            search_word = self.get_argument('search_word')
            server_data = AllMachineInfo.search_hosts_quick(search_word.strip())
            server_data_handled = DataManage.manage_machine_list(server_data)
            server_length = len(server_data_handled)
            page = self.get_argument("page", default="1")
            self.render('machines/main.html', name=settings.template_variables, server_data=server_data_handled,
                        server_length=server_length, page=int(page))
        elif self.get_argument('search') == 'high':
            select_data = AllMachineInfo().add_host_select
            select_data_handled, status_handled = DataManage.manage_add_host_select(select_data)
            self.render('machines/search_hosts.html', name=settings.template_variables, select_data=select_data_handled,
                        select_data_status=status_handled)
        elif self.get_argument('search') == 'distribute':
            project_name = self.get_argument('project_name')
            server_data = AllMachineInfo.distribute_host_search(project_name)
            server_data_handled = DataManage.manage_machine_list(server_data)
            server_length = len(server_data_handled)
            page = self.get_argument("page", default="1")
            self.render('machines/main.html', name=settings.template_variables, server_data=server_data_handled,
                        server_length=server_length, page=int(page))

    def post(self, *args, **kwargs):
        data_dic = dict()
        data_list = settings.ADD_HOST_LIST
        for name in data_list:
            data_dic[name] = self.get_argument(name)
        server_data = AllMachineInfo.search_hosts(data_dic)
        server_data_handled = DataManage.manage_machine_list(server_data)
        server_length = len(server_data_handled)
        page = self.get_argument("page", default="1")
        self.render('machines/main.html', name=settings.template_variables, server_data=server_data_handled,
                    server_length=server_length, page=int(page))


class HostDistribute(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        data_distribute, data_nums = AllMachineInfo().distribute_host
        data_distribute_handled = DataManage.manage_host_distribute(data_distribute)
        self.render("machines/host_distribute.html", name=settings.template_variables,
                    data_distribute=data_distribute_handled, data_nums=data_nums[0][0])


