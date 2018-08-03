#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ADNAP7

from django.http import  HttpResponse
from article.models import Article

#数据库操作
def testdb(request):
    # test1=Article(title='Hello World',category='Python',content='我们来做一个简单的数据库增加操作')
    # test1.save()
    # test1 = Article(title='Django Blog学习', category='Python', content='Django简单博客教程')
    # test1.save()
    # return HttpResponse("<p>数据库操作成功</p>")

    # response1=""
    # list=Article.objects.all()
    # for var in list:
    #     response1=response1+var.title
    # return HttpResponse("<p>"+response1+"</p")



    # response2=Article.objects.get(id=1)
    # return HttpResponse("<p>" + response2.title+ "</p")

    # response3=Article.objects.get(id=1)
    # response3.content="Hello World,How are you"
    # response3.save()
    # return HttpResponse("更新第1行数据成"+response3.content)

    response4=Article.objects.get(id=1).delete()
    return HttpResponse("删除成功")




