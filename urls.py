#coding:utf-8

from handlers.machines import MachineList, AddHost, ModifyHost

urls = [
    (r"/", MachineList),
    (r"/addhost", AddHost),
    (r"/mhost", ModifyHost),
]