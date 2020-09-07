#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "yang";

'''
该 Django 项目的 URL 声明，一份由 Django 驱动的网站"目录"；
函数作为参数传递，不加括号，相当于绑定事件，事件触发再执行
path路径末尾带/，Django中设置了APPEND_SLASH=True, 当URL后面缺少斜杠时，会自动拼上斜杠，并重定向
'''
from django.contrib import admin
from django.urls import path,re_path
from test_app import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'helloworld/',views.hello_world),
    path(r'test/index', views.test_index),
    path('user/', views.insert_user),
    path('index/', views.index),
    path('indexSimple/', views.index_simple),
    # re_path(r'^hello_world$',views.hello_world),
    # url(r'^hello_world$', views.hello_world),
]
