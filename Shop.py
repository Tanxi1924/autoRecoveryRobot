from email import message
import json
import random
import re
from typing import List,Literal

from nonebot import on_command,on_keyword,on_message,on_fullmatch
from nonebot.internal.adapter import bot
from nonebot.internal.params import Arg
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import GroupMessageEvent, PrivateMessageEvent, MessageEvent,Message,Bot,MessageSegment
from nonebot.log import logger
from nonebot.params import CommandArg

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.executors.pool import ThreadPoolExecutor

from .data_handle import * #导入数据处理包
from .items_handle import * #导入物品包
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.params import ArgPlainText, CommandArg


shop=on_fullmatch(["查看市场布告板","查看布告板","打开市场布告板","打开布告板"],priority=20,block=True)
refresh=on_fullmatch(["刷新市场布告板","刷新布告板"],priority=20,block=True)


@shop.handle()
async def createShop(event: Event):
    uid=str(event.user_id)
    favor=readData(uid)
    shoppinglist=getShoppingList(uid)
    nickName=readName(uid)
    msg=f"{nickName}大人，市场现在有\n"
    print(shoppinglist)
    j=1
    for value in shoppinglist:
        str1=getItemDetail(value)
        name=str1['ItemName']
        money=str1['Money']
        msg+=f"{j}：商品名:{name}  {money}金币\n"
        j+=1
    await shop.send(Message(msg))

@shop.got("key")
async def Create(event: Event,id: str = ArgPlainText("key")):
    uid = event.get_user_id()
    shoppinglist=getShoppingList(uid)
    Nickname=readName(uid)
    money=int(readTargetData(uid,"Money"))
    try:
     shopId=int(id)-1
    except EOFError:
     print(1)
     await shop.finish(Message("某位大人…我、我没有找到您想买的东西…对不起，请您再核对一下呢？（购物失败）"))
    if(shopId<=len(shoppinglist)+1 and shopId>=0):
        itemId=shoppinglist[shopId]
        Dict=getItemDetail(itemId)
        itemMoney=Dict['Money']
        name=Dict['ItemName']
        if(money<itemMoney):
            await shop.finish(Message(f"{Nickname}大人！！您的荷包已经空空了…没有钱买{name}了呀！请您努力赚钱！"),at_sender=True)
        else:
            addTargetData(uid,"Money",-itemMoney)
            setShoppingList(uid,id)
            print(id)
            add_item(uid,itemId,1)
            await shop.finish(Message(f"{Nickname}大人，已经给您买回来{name}啦…您要现在看看吗？"),at_sender=True)
    await shop.finish(Message("某位大人…我、我没有找到您想买的东西…对不起，请您再核对一下呢？（购物失败）"))
@refresh.handle()
async def _(event: Event):
    uid=str(event.user_id)
    Nickname=readName(uid)
    if(readTargetData(uid,"Refresh")>0):
        addTargetData(uid,"Refresh",-1)
        createShoppingList(uid)
        await refresh.finish(Message(f"{Nickname}大人，市场进新货了~！"),at_sender=True)
    else:
        await refresh.finish(Message(f"{Nickname}大人，薇尔莉特好累…一会儿再去好不好？"),at_sender=True)





