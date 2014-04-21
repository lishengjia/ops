#coding:utf-8
import time
import os
import tornado.web

from ops.model.base import BaseHandler
from ops import settings
from ops.model.machines.mysql_opertation import AllMachineInfo
from ops.model.machines.data_manage import DataManage
from ops.model.check import Check


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
        if self.get_argument("server_select_status"):
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


class HostExport(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        server_data = AllMachineInfo().machine_list
        server_data_handled = DataManage.manage_machine_list(server_data)
        DataManage.manage_host_export(server_data_handled)
        self.add_header("Content-Type", "application/vnd.ms-excel")
        self.add_header("Content-Disposition", "attachment;filename=machine.xls")
        self.render("../download/machine.xls")
        os.system("rm -rf download/machine.xls")


class RoomList(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        room_data, room_count = AllMachineInfo.room_list()
        room_data_handled, room_data_count_handled = DataManage.manage_room_list(room_data, room_count)
        self.render("machines/room_list.html", name=settings.template_variables, room_data=room_data_handled,
                    room_count=room_data_count_handled)


class RoomModify(BaseHandler):
    rid = ""

    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        action = self.get_argument("action")
        RoomModify.rid = self.get_argument("rid")
        if action == "modify":
            single_room_data = AllMachineInfo.get_room_modify(RoomModify.rid)
            self.render("machines/modify_room.html", name=settings.template_variables, single_room_data=single_room_data[0])
        elif action == "delete":
            AllMachineInfo.delete_room_modify(RoomModify.rid)
            self.write("<script language='javascript'>window.location.href='/roomlist';</script>")


    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        contact_list = ["room_name", "room_contact", "contact_phone", "room_comment"]
        contact_dict = dict()
        for contact in contact_list:
            contact_dict[contact] = self.get_argument(contact)
        check_result = Check.room_check(contact_dict, False)
        if check_result == "ok":
            AllMachineInfo.set_room_modify(contact_dict, RoomModify.rid)
            self.write("<script language='javascript'>alert('修改完成');window.location.href='/roomlist';</script>")
        else:
            self.write(check_result)


class AddRoom(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("machines/add_room.html", name=settings.template_variables)

    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        contact_data = dict()
        contact_list = ["room_name", "room_contact", "contact_phone", "room_comment"]
        for contact in contact_list:
            contact_data[contact] = self.get_argument(contact)
        check_result = Check.room_check(contact_data, True)
        if check_result == "ok":
            AllMachineInfo.set_add_room(contact_data)
            self.write("<script language='javascript'>alert('添加完成');window.location.href='/roomlist';</script>")
        else:
            self.write(check_result)


class ProjectManage(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        action = self.get_argument("action", default="list")
        if action == "list":
            project_list = AllMachineInfo.get_project_list()
            project_list_handled = DataManage.manage_project_list(project_list)
            self.render("machines/projectlist.html", name=settings.template_variables, project_list=project_list_handled)
        elif action == "delete":
            pid = self.get_argument("pid")
            AllMachineInfo.delete_project(pid)
            self.write("<script language='javascript'>window.location.href='/projectmanage';</script>")

    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        project_name = self.get_argument("project_name")
        check_result = Check.project_check(project_name)
        if check_result == "ok":
            AllMachineInfo.set_add_project(project_name)
            self.write("<script language='javascript'>alert('添加完成');window.location.href='/projectmanage';</script>")
        else:
            self.write(check_result)


class ContactManage(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        action = self.get_argument("action", default="list")
        if action == "list":
            contact_list = AllMachineInfo.get_contact_list()
            contact_list_handled = DataManage.manage_contact_list(contact_list)
            self.render("machines/contact_list.html", name=settings.template_variables, contact_list=contact_list_handled)
        elif action == "delete":
            cid = self.get_argument("cid")
            AllMachineInfo.delete_contact(cid)
            self.write("<script language='javascript'>window.location.href='/contactmanage?action=list';</script>")

    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        contact_info = dict(contact_name=self.get_argument("contact_name"), contact_info=self.get_argument("contact_info"))
        check_result = Check.contact_check(contact_info)
        if check_result == "ok":
            AllMachineInfo.set_add_contact(contact_info)
            self.write("<script language='javascript'>alert('添加完成');window.location.href='/contactmanage';</script>")
        else:
            self.write(check_result)