from index.models import User
from django.shortcuts import HttpResponse

class UserAuth():

    def __init__(self):
        pass

    @staticmethod
    def is_login(req):   # 是否登录

        if req.session.get('is_login',False) and req.session.get('user_name',False):
            return True
        else:
            return False


    @staticmethod
    def out_login(req):           # 用户登出
        req.session.delete()
        return True

    @staticmethod
    def login(req,user_name):      # 用户登录

       req.session['is_login'] = True
       req.session['user_name'] = user_name
       return True

    @staticmethod
    def get_login(req):   #获取用户登录状态

        if req.session.get('is_login', None):
            if req.session['is_login'] == True:
                retUser = {
                    'is_login': True,
                    'username': req.session['user_name']
                }
                return retUser
            else:
                return False
        else:
            return False
