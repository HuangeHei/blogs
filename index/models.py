from django.db import models

# Create your models here.


class Article(models.Model):

    Article_Title = models.CharField(max_length=1024)
    Aritcle_Text = models.CharField(max_length=102400)
    Aritcle_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Article_Title



class User(models.Model):

    User_Name = models.CharField(max_length=1024)
    User_Passwd = models.CharField(max_length=1024)
    User_Aritcle = models.ManyToManyField(Article,null=True,blank=True)

    def __str__(self):
        return self.User_Name



