#coding:utf-8
import tornado.web

from modules.base import BaseHandler
import settings
from modules.users.mysql_opertation import UserSqlOperation
from modules.users.data_manage import UserDataManage
from modules.check import Check


class Login(BaseHandler):
    origin_url = ""

    def get(self, *args, **kwargs):
        Login.origin_url = self.get_argument("next")
        self.render("users/login.html", login_strings=dict(username="Username", password="Password"))

    def post(self, *args, **kwargs):
        input_username = self.get_argument("username")
        input_password = self.get_argument("password")
        check_result = Check.login_check(input_username, input_password)
        if check_result == "Invalid username":
            self.render("users/login.html", login_strings=dict(username="Invalid username", password="Password"))
        elif check_result == "ok":
            self.set_secure_cookie(settings.cookie_name, input_username)
            self.redirect(Login.origin_url)
        elif check_result == "Incorrect password":
            self.render("users/login.html", login_strings=dict(username="Username", password="Incorrect password"))
        else:
            self.redirect("/login?next=/")


class Logout(BaseHandler):
    def get(self, *args, **kwargs):
        self.clear_cookie(settings.cookie_name)
        self.redirect("/login?next=/")


class UserList(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        user_data = UserSqlOperation().user_list
        user_data_handled = UserDataManage.manage_user_list(user_data)
        self.render("users/user_list.html", name=settings.template_variables, user_data=user_data_handled)


class UserModify(BaseHandler):
    uid = ""

    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        UserModify.uid = self.get_argument("uid")
        action = self.get_argument("action")
        if action == "modify":
            user_data = UserSqlOperation.user_modify(UserModify.uid)
            user_data_handled = UserDataManage.manage_user_list(user_data)
            self.render("users/user_modify.html", name=settings.template_variables, user_data=user_data_handled)
        elif action == "delete":
            UserSqlOperation.user_delete(UserModify.uid)
            js_str = "<script language='javascript'>window.location.href='/userlist';</script>"
            self.write(js_str)

    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        data_dic = dict(user_name="", user_password="")
        for data in data_dic.keys():
            data_dic[data] = self.get_argument(data)
        result = Check.user_modify_check(data_dic, False)
        if result == "ok":
            data_dic["user_password"] = Check.md5(data_dic["user_password"])
            UserSqlOperation.user_modify_update(data_dic, UserModify.uid)
            self.write("<script language='javascript'>alert('修改完成');window.location.href='/userlist';</script>")
        elif result == "md5":
            UserSqlOperation.user_modify_update(data_dic, UserModify.uid)
            self.write("<script language='javascript'>alert('修改完成');window.location.href='/userlist';</script>")
        else:
            return self.write(result)


class AddUser(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("users/add_user.html", name=settings.template_variables)

    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        user_data = dict()
        user_data["user_name"] = self.get_argument("user_name")
        user_data["user_password"] = self.get_argument("user_password")
        result = Check.user_modify_check(user_data, True)
        if result == "ok":
            user_data["user_password"] = Check.md5(user_data["user_password"])
            print user_data
            UserSqlOperation.add_user(user_data)
            self.write("<script language='javascript'>alert('添加完成');window.location.href='/adduser';</script>")
        else:
            return self.write(result)
