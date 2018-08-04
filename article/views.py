from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
from article.models import Article


# def home(request):
#     return HttpResponse("Hello,Django")

# def detail(request,my_args):
#     # return HttpResponse("You're looking at my_args %s." % my_args)              #该句语法像极了c中的输出语句
#
#     post = Article.objects.all()[int(my_args)]                                    #检索一个
#     str = ("title=%s,category=%s,date_time=%s,content=%s" % (post.title, post.category, post.date_time, post.content))
#     return HttpResponse(str)

def test(request):
    return render(request,'test.html',{'current_time':datetime.now()})

def home(request):
    post_list=Article.objects.all()
    return render(request,'home.html',{'post_list':post_list})

def detail(request,id):
    try:
        post=Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,'post.html',{'post':post})

