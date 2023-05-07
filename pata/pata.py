# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from airtest.core.settings import Settings as ST

# 设置全局阙值为0.8
ST.THRESHOLD = 0.8
ST.CVSTRATEGY = ["sift"]
ST.FIND_TIMEOUT = 2
import logging

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

auto_setup(__file__, devices=[
    "android://127.0.0.1:5037/127.0.0.1:7555?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH"])
for i in range(150):

    try:
        print("继续挑战")
        touch(Template(r"tpl1681443263777.png", record_pos=(-0.004, 0.52), resolution=(810, 1440)))

    except:
        pass
    sleep(6)
    print("点击跳过战斗")
    tiaoguozhandou = exists(Template(r"tpl1679290497442.png", record_pos=(0.001, 0.621), resolution=(720, 1280)))
    if tiaoguozhandou:
        touch(tiaoguozhandou)
    try:
        print("点击任意地方关闭")
        guanbi = wait(Template(r"tpl1680512074011.png", record_pos=(-0.001, 0.649), resolution=(810, 1440)))
        touch(guanbi)
    except:
        pass

    wuping_list = [
        exists(Template(r"tpl1679288227707.png", rgb=True, record_pos=(0.001, 0.212), resolution=(720, 1280))),
        exists(Template(r"tpl1679289710688.png", rgb=True, record_pos=(0.178, 0.212), resolution=(720, 1280))),
        exists(Template(r"tpl1679289853881.png", rgb=True, record_pos=(0.178, 0.212), resolution=(720, 1280))),
        exists(Template(r"tpl1679289901396.png", rgb=True, record_pos=(-0.178, 0.212), resolution=(720, 1280))),
        exists(Template(r"tpl1679289915480.png", rgb=True, record_pos=(-0.001, 0.204), resolution=(720, 1280))),
        exists(Template(r"tpl1679290217667.png", rgb=True, record_pos=(0.182, 0.212), resolution=(720, 1280))),
        exists(Template(r"tpl1679373973639.png", rgb=True, record_pos=(0.188, 0.211), resolution=(720, 1280))),
        exists(Template(r"tpl1679374294099.png", rgb=True, record_pos=(0.178, 0.215), resolution=(720, 1280)))

    ]

    is_click = list(filter(lambda x: x is not False, wuping_list))
    print(1,is_click)
    if is_click:
        is_click = list(filter(lambda x: x[1] > 760, is_click))
        print(2,is_click)
        if is_click:
            print("点击确定")
            touch(is_click[0])
            try:
                touch(Template(r"tpl1681444380623.png", record_pos=(0.184, 0.579), resolution=(810, 1440)))

            except:
                pass

        else:
            print("点击放弃")
            try:
                touch(Template(r"tpl1681444346192.png", record_pos=(-0.188, 0.584), resolution=(810, 1440)))

            except:
                pass


    else:
        try:
            print("点击放弃")
            touch(Template(r"tpl1681444346192.png", record_pos=(-0.188, 0.584), resolution=(810, 1440)))
        except:
            pass
    sleep(2)
