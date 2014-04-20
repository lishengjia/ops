#coding:utf-8

from ops.handlers.machines import MachineList, AddHost, ModifyHost, SearchHosts, HostDistribute, \
    HostExport, RoomList, RoomModify,  AddRoom, ProjectManage, ContactManage
from ops.handlers.user import Login, Logout, UserList, UserModify, AddUser

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
    (r"/export", HostExport),
    (r"/roomlist", RoomList),
    (r"/roommodify", RoomModify),
    (r"/addroom", AddRoom),
    (r"/projectmanage", ProjectManage),
    (r"/contactmanage", ContactManage),
]