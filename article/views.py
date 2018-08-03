from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from article.models import Article


def home(request):
    return HttpResponse("Hello,Django")

def detail(request,my_args):
    # return HttpResponse("You're looking at my_args %s." % my_args)              #该句语法像极了c中的输出语句

    post = Article.objects.all()[int(my_args)]                                    #检索一个
    str = ("title=%s,category=%s,date_time=%s,content=%s" % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)

