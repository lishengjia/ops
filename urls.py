#coding:utf-8

from handlers.machines import MachineList, AddHost, ModifyHost, SearchHosts, HostDistribute
from handlers.user import Login, Logout, UserList, UserModify, AddUser

urls = [
    (r"/login", Login),
    (r"/logout", Logout),
    (r"/", MachineList),
    (r"/addhost", AddHost),
    (r"/mhost", ModifyHost),
    (r"/shosts", SearchHosts),
    (r"/distribute", HostDistribute),
    (r"/userlist", UserList),
    (r"/usermodify", UserModify),
    (r"/adduser", AddUser),
]