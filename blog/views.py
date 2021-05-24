import random
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,View,DetailView
from django.core.mail import send_mail
from bycarlosalas.settings import EMAIL_HOST_USER
from .models import Comment,Post,Category,SocialMedia,Web,Subscriber
from .utils import *
from .forms import ContactForm, CommentForm

class Blog(ListView):

    def get(self,request,*args,**kwargs):
        posts = list(Post.objects.filter(
                status = True,
                published = True
                ).values_list('id',flat = True))
        main = random.choice(posts)
        posts.remove(main)
        main = consult(main)

        post1 = random.choice(posts)
        posts.remove(post1)
        post2 = random.choice(posts)
        posts.remove(post2)
        post3 = random.choice(posts)
        posts.remove(post3)
        post4 = random.choice(posts)
        posts.remove(post4)
        post5 = random.choice(posts)
        posts.remove(post5)
        post6 = random.choice(posts)
        posts.remove(post6)

        try:
            post_tecnologia = Post.objects.filter(
                                status = True,
                                published = True,
                                category = Category.objects.get(name = 'tecnologia')
                                ).latest('publication_date')
        except:
            post_tecnologia = None

        try:
            post_general = Post.objects.latest('publication_date')
        except:
            post_general = None

        context = {
            'main':main,
            'post1': consult(post1),
            'post2': consult(post2),
            'post3': consult(post3),
            'post4': consult(post4),
            'post5': consult(post5),
            'post6': consult(post6),
            'post_general':post_general,
            'post_tecnologia':post_tecnologia,
            'socialmedia':getSocialMedia(),
            'web':getWeb(),
        }

        return render(request,'blog.html',context)

class List(ListView):

    def get(self,request,category_name,*args,**kwargs):
        context = ganerateCategory(request,category_name)
        return render(request,'category.html',context)

class ContactForm(View):
    def get(self,request,*args,**kwargs):
        form = ContactForm()
        context = {
            'socialmedia':getSocialMedia(),
            'web':getWeb(),
            'form':form,
        }
        return render(request,'contact.html',context)

    def post(self,request,*args,**kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
        else:
            context = {
                'form':form,
            }
            return render(request,'contact.html',context)

class PostDetail(DetailView):
    def get(self,request,*args,**kwargs):
        try:
            post = Post.objects.get(pk=kwargs['pk'])
        except:
            post = None
        posts = list(Post.objects.filter(
                status = True,
                published = True
                ).values_list('id',flat = True))
        posts.remove(post.id)
        post1 = random.choice(posts)
        posts.remove(post1)
        post2 = random.choice(posts)
        posts.remove(post2)
        post3 = random.choice(posts)
        posts.remove(post3)

        context = {
            'post':post,
            'socialmedia':getSocialMedia(),
            'web':getWeb(),
            'post1':consult(post1),
            'post2':consult(post2),
            'post3':consult(post3),
        }
        return render(request,'post.html',context)

class Subscribe(View):
    def post(self,request,*args,**kwargs):
        email = request.POST.get('correo')
        Subscribe.objects.create(email = email)
        subject = 'GRACIAS POR SUSCRIBIRTE A BLOG.DEV!'
        message = 'Te haz suscrito exitosamente a Blog.Dev, Gracias por tu preferencia!!!'
        try:
            send_mail(subject,message,EMAIL_HOST_USER,[email])
        except:
            pass

        return redirect('base:index')

class ListComments(ListView):

    def get(self,request,id,*args,**kwargs):
        context = ganerateComments(request,id)
        return render(request,'post.html',context)

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})

