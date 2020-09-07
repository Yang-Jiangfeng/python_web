#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "yang";

'''
该应用的一些配置，Django-1.9会自动已生成，之前的版本没有；
'''
from django.apps import AppConfig


class TestAppConfig(AppConfig):
    name = 'test_app'
