from django.urls import path
from . import views
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('blog',Blog.as_view(), name = 'blog'),
    path('vida/',List.as_view(),{'category_name':'vida'}, name = 'vida'),
    path('finanzas/',List.as_view(),{'category_name':'finanzas'}, name = 'finanzas'),
    path('marketing/',List.as_view(),{'category_name':'marketing'}, name = 'marketing'),
    path('ecommerce/',List.as_view(),{'category_name':'ecommerce'}, name = 'ecommerce'),
    path('dev-web/',List.as_view(),{'category_name':'dev-web'}, name = 'dev-web'),
    path('criptomonedas/',List.as_view(),{'category_name':'criptomonedas'}, name = 'criptomonedas'),
    path('crecimiento/',List.as_view(),{'category_name':'crecimiento'}, name = 'crecimiento'),
    path('emprendimiento/',List.as_view(),{'category_name':'emprendimiento'}, name = 'emprendimiento'),
    path('productividad/',List.as_view(),{'category_name':'productividad'}, name = 'productividad'),
    path('tecnologia/',List.as_view(),{'category_name':'tecnologia'}, name = 'tecnologia'),
    path('contact_form/', ContactForm.as_view(), name = 'contact_form'),
    path('subscribe/',Subscribe.as_view(), name = 'subscribe'),
    path('post/<slug:slug>/',PostDetail.as_view(), name = 'post_detail'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
]