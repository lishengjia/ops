#coding:utf-8

from handlers.machines import MachineList, AddHost, ModifyHost, SearchHosts, HostDistribute, Login, Logout

urls = [
    (r"/login", Login),
    (r"/logout", Logout),
    (r"/", MachineList),
    (r"/addhost", AddHost),
    (r"/mhost", ModifyHost),
    (r"/shosts", SearchHosts),
    (r"/distribute", HostDistribute),
]