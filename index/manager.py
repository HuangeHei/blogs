from index.models import User,Article

import json


class ArticleManager():
    '''
        如果传入user_id 则取一个人，如果没有则取全部
    '''
    @staticmethod
    def to_json(user_name,id=False):


        ret = []

        u_obj = User.objects.filter(User_Name = user_name)

        if id == False:
            objects = u_obj[0].User_Aritcle.all()
        else:
            objects = Article.objects.filter(id = id)

        for item in objects:

            _item = {}
            _item['article_id'] = item.id
            _item['article_title'] = item.Article_Title
            _item['article_text'] = item.Aritcle_Text
            _item['article_date'] = item.Aritcle_Date.strftime("%Y-%m-%d %H:%M:%S")

            ret.append(_item)

        return json.dumps(ret)



class UserManager():
    '''
        如果传入user_id 则取一个人，如果没有则取全部
    '''
    @staticmethod
    def to_json(user_id = False):


        ret = []

        if user_id:

            objects = User.objects.filter(id = user_id)

        else:

            objects = User.objects.all()



        for item in objects:

            _item = {}
            _item['user_id'] = item.id
            _item['user_name'] = item.User_Name

            ret.append(_item)

        return json.dumps(ret)

