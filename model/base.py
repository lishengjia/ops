#coding:utf-8
import tornado.web
from ops import settings


class BaseHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        settings.template_variables["login_username"] = self.get_secure_cookie(settings.cookie_name)
        return self.get_secure_cookie(settings.cookie_name)