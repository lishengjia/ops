#coding:utf-8

from handlers.machines import MachineList, AddHost, ModifyHost, SearchHosts, HostDistribute

urls = [
    (r"/", MachineList),
    (r"/addhost", AddHost),
    (r"/mhost", ModifyHost),
    (r"/shosts", SearchHosts),
    (r"/distribute", HostDistribute)
]