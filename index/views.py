from django.shortcuts import render,HttpResponse
from django.views import View
from common.UserAuth import UserAuth
from index.models import User,Article
from index.manager import ArticleManager,UserManager
import json
# Create your views here.

# 用户 登录 登出

'''
    /login get 方式无需参数
    
    :return 有登录信息
    {
        'is_login': True,
        'username': req.session['user_name']
    }
    :return 无登录信息
    {
        false
    }
    
    /login post
    参数 username
    参数 userpasswd
    
    :return 成功
    {
       'ok' 
    }
    :return 失败
    {
        'error'
    }
    
'''

class Login(View):
    '''
        访问 Login
    '''

    def get(self, request):

        return HttpResponse(json.dumps(UserAuth.get_login(request)))

    def post(self, request):
        try:
            # 不跳异常那么就是查询到了 跳异常拦截直接error
            print(request.POST['username'],request.POST['userpasswd'])
            User.objects.get(User_Name=request.POST['username'], User_Passwd=request.POST['userpasswd'])
            UserAuth.login(request, request.POST['username'])
            return HttpResponse('ok')

        except Exception as E:
            print(E)
            return HttpResponse('error')


'''
    /out get 方式无需参数
    :return
    {
        True
    }

'''

class Out(View):

    def get(self, request):
        return HttpResponse(json.dumps(UserAuth.out_login(request)))

    def post(self, request):
        pass


'''
    /userlist get 方式无需参数 获取数据库内所有用户信息
    :return
    [{
        user_id:'123'
        user_name:'123'
    }]
    
'''

class UserList(View):

    def get(self, request):

        return HttpResponse(UserManager.to_json())


'''
    /userarticlelist get 参数 user_name 
    :return
    [{
        article_id:'123'
        article_title:'标题'
        article_text:'内容'
        article_date:'2018-5-17 17:57:52'
    }]

'''

class UserArticleList(View):

    def get(self, request):
        user_name = request.GET['user_name']
        if  user_name:
            return HttpResponse(ArticleManager.to_json(user_name=user_name))
        else:
            return HttpResponse('error')





'''
    /articles get 参数 article_id
    :return
    [{
        article_id:'123'
        article_title:'标题'
        article_text:'内容'
        article_date:'2018-5-17 17:57:52'
    }]

'''
class Articles(View):
    def get(self, request):
        return HttpResponse(ArticleManager.to_json(0,id = request.GET['article_id']))


