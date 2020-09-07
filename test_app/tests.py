#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "yang";

'''
自动化测试模块，可以利用脚本进行自动化测试；
'''

from django.test import TestCase
import random,datetime
from django.core import serializers
# Create your tests here.
from django.http import HttpResponse,JsonResponse

from test_app.models import User;

# Create your tests here.
def test_db(request):
    # 插入数据
    user_model = User(user_name="yang" + str(random.randint(1, 10)), password="111",
                      create_date=datetime.datetime.now())
    user_model.save();

    users = User.objects.all()
    print("==== 查询所有 ====", users)

    users = User.objects.filter(id=1)
    print("==== 条件查询 ====", users)

    user = User.objects.get(id=1)
    print("==== 获取单个对象 ====", user)

    # 更新数据
    user.user_name = "yang" + str(random.randint(1, 10))
    user.save()

    users = serializers.serialize("json", User.objects.order_by("user_name")[0, 2])
    print("==== 排序&limit ====" + users)