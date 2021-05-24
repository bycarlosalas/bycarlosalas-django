from django.core.paginator import Paginator
from .models import Comment,Post,Category,SocialMedia,Web

def consult(id):
    try:
        return Post.objects.get(id = id)
    except:
        return None

def getSocialMedia():
    return SocialMedia.objects.filter(status = True).latest('creation_date')

def getWeb():
    return Web.objects.filter(status = True).latest('creation_date')

def ganerateCategory(request,category_name):
    posts = Post.objects.filter(
                        status = True,
                        published = True,
                        category = Category.objects.get(name = category_name)
                        )
    try:
        category = Category.objects.get(name = category_name)
    except:
        category = None

    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'posts':posts,
        'socialmedia':getSocialMedia(),
        'web':getWeb(),
        'category':category,
    }
    return context

def ganerateComments(request,id):
    comments = Comment.objects.filter(
                        status = True,
                        published = True,
                        comment = Comment.objects.get(name = id)
                        )
    try:
        comment = Comment.objects.get(name = id)
    except:
        comment = None

    paginator = Paginator(comments,3)
    page = request.GET.get('page')
    comments = paginator.get_page(page)
    context = {
        'comments':comments,
        'comment':comment,
    }
    return context
