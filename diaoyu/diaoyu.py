# -*- encoding=utf8 -*-
__author__ = "Administrator"

import logging
from airtest.core.api import *
from airtest.core.settings import Settings as ST

ST.CVSTRATEGY = ["sift"]
ST.FIND_TIMEOUT = 2

auto_setup(__file__, devices=[
    "android://127.0.0.1:5037/127.0.0.1:7555?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH"])

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

# shengyu = exists(Template(r"tpl1680509365011.png", record_pos=(-0.34, -0.817), resolution=(810, 1440)))
# print(f"现在剩余的钓鱼次数为 {shengyu} 是false的石头就是0 ")

scene1 = exists(Template(r"tpl1683438627156.png", record_pos=(-0.025, 0.253), resolution=(720, 1280)))

scene2 = exists(Template(r"tpl1683438980476.png", record_pos=(-0.111, 0.257), resolution=(720, 1280)))

for i in range(200):
    if scene1:

        try:
            # 鱼鳔
            if exists(Template(r"tpl1683438771992.png", record_pos=(-0.121, 0.243), resolution=(720, 1280))):
                print("当前页面发现鱼鳔,点击进行钓鱼...")
                touch((381, 966))
                sleep(12)
            else:
                print("鱼漂被挡住了,点击页面任何位置")
                touch((400, 1360))
        except:
            pass
    elif scene2:

        try:
            # 鱼鳔
            if exists(Template(r"tpl1683439043378.png", record_pos=(-0.14, 0.247), resolution=(720, 1280))):
                print("当前页面发现鱼鳔,点击进行钓鱼...")
                touch((381, 966))
                sleep(12)
            else:
                print("鱼漂被挡住了,点击页面任何位置")
                touch((400, 1360))
        except:
            pass

    try:
        sleep(2)
        print("点击出售")
        touch(Template(r"tpl1681177388380.png", record_pos=(-0.177, 0.641), resolution=(810, 1440)))
        sleep(1)
    except:
        pass

    try:
        sleep(1)

        touch(Template(r"tpl1681177340320.png", record_pos=(0.19, 0.202), resolution=(810, 1440)))

        print("点击确定")
        sleep(1)
    except:
        pass

    try:
        touch(Template(r"tpl1681176483224.png", record_pos=(-0.18, 0.642), resolution=(810, 1440)))

        print("点击订单提交")

    except:
        pass

