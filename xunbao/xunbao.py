# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
ST.CVSTRATEGY = ["sift"]
ST.FIND_TIMEOUT = 2

auto_setup(__file__, devices=[
    "android://127.0.0.1:5037/127.0.0.1:7555?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH"])
for i in range(3):
    try:
        touch(Template(r"tpl1680586307725.png", record_pos=(-0.401, 0.649), resolution=(810, 1440)))
    except:
        pass

    try:
        touch(Template(r"tpl1680586323156.png", record_pos=(-0.299, 0.4), resolution=(810, 1440)))
    except:
        pass

    try:
        touch(Template(r"tpl1680586342313.png", record_pos=(-0.326, 0.642), resolution=(810, 1440)))
    except:
        pass

    try:
        touch(Template(r"tpl1680586354003.png", record_pos=(0.191, 0.19), resolution=(810, 1440)))
        sleep(35)
    except:
        pass

    try:

        touch(Template(r"tpl1680586423577.png", record_pos=(0.425, -0.821), resolution=(810, 1440)))


    except:
        pass
    sleep(120)

