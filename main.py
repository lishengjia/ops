#coding:utf-8

import tornado.ioloop
import tornado.web
from applications import application, PORT

if __name__ == "__main__":
    application.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()