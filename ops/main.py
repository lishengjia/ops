#coding:utf-8

import tornado.ioloop
import tornado.web
from ops.applications import application, PORT
import signal


def init_settings():
    from tornado.options import define, options, parse_command_line

    # 加载环境配置项
    define("port", default=PORT, type=int, help=u'监听端口')

    parse_command_line()
    return options


def start_application():
    options = init_settings()
    print 'serve listen port %s' % options.port

    application.listen(options.port)

    def stop_handler(sig, frame):
        tornado.ioloop.IOLoop.instance().stop()

    signal.signal(signal.SIGTERM, stop_handler)
    signal.signal(signal.SIGINT, stop_handler)

    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    start_application()
