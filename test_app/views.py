#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "yang";

'''
视图模块，执行相应的代码所在的模块，代码逻辑处理的主要地点，项目大部分代码均在这里编写；
'''

from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,JsonResponse
from test_app.models import *;
import random,datetime,json;

def hello_world(request):
    return HttpResponse("Hello World");

def insert_user(request):
    user = User(user_name="hujiang" + str(random.randint(1, 10)), password="111111",
                      create_date=datetime.datetime.now())
    # user.save();

    user = User.objects.get(id=1);
    print(type(user))

    user_json = serializers.serialize("json", [user]);

    return JsonResponse(json.loads(user_json), safe=False);

def index(request):
    contex = {};
    return render(request, "index.html", contex);

def index_simple(request):
    contex = {};
    return render(request, "indexSimple.html", contex);

def test_index(request):
    contex = {};
    contex["name"] = "yang";
    contex["name_list"] = ["yang", "jiang", "feng"];
    contex["person"] = {"name":"yang","age":22};
    contex["birthday"] = datetime.datetime.now();
    contex["number"] = '2048';
    contex["url"] = 'http://www.baidu.com';
    contex["isman"] = True;
    contex["age"] = 20;
    return render(request, "test/index.html", contex);