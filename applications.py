#coding:utf-8

import tornado.ioloop
import tornado.web
import os
from urls import urls


PORT = 8888

SETTINGS = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    login_url="/login",
    cookie_secret="234lksjfASKJFlks=jdfGLKS=JDFLKSsfjlk234dsjflksdjffj/=sf"
)

application = tornado.web.Application(
    handlers=urls,
    **SETTINGS
)