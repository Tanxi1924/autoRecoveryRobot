from asyncio import sleep

from nonebot.internal.matcher import Matcher
from nonebot.plugin import on_regex, on_fullmatch,on_message,on_keyword,on_startswith

from nonebot import on_notice
from nonebot.adapters.onebot.v11 import PokeNotifyEvent, Message, MessageSegment,GroupIncreaseNoticeEvent
import nonebot.matcher
import sys
sys.path.append(r'C:\Users\Administrator\first\src')
from plugin_whateat_pic import eat
from .Shop import *
from nonebot import require
from nonebot_plugin_tts_gal import *
from email import message
import json
import random
import re
from typing import List,Literal
from nonebot import on_command,on_keyword,on_message
from nonebot.internal.adapter import bot
from nonebot.adapters.onebot.v11 import GroupMessageEvent, PrivateMessageEvent, MessageEvent,Message,Bot,MessageSegment
from nonebot.log import logger
from nonebot.params import CommandArg
from .data_handle import * #导入数据处理包
from .items_handle import * #导入物品包
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot import on_message,on_fullmatch
import datetime as dt
from dateutil import parser
from dateutil import rrule


def _check(event: PokeNotifyEvent):
    return event.target_id==event.user_id

agree_list=[750121182]

pokelistadd=on_regex(r"^/pokelist\s+join\s+\d+")
itemrandom=on_command("刷新概率列表",permission=SUPERUSER)

@itemrandom.handle()
async def _(event: Event):
    createrandom_item()


@pokelistadd.handle()
async def _(event: Event):
    msg = event.get_plaintext()
    msg = re.sub(r"^/pokelist\s+join\s+", '', msg)
    id = int(msg)
    if(event.user_id in agree_list):
        pass
    else:
        await pokelistadd.finish(Message(f"[CQ:at,qq={event.user_id}]但您不能成为猫娘的主人"))



def _rule(event: Event):
    return isinstance(event, GroupIncreaseNoticeEvent)

join=on_notice(rule=_rule)
@join.handle()
async def group_increase_handle(event: GroupIncreaseNoticeEvent,bot: Bot):
    info=await bot.get_group_member_info(group_id=event.group_id,user_id=event.user_id,no_cache=False)
    card=info.get("nickname")
    await join.send(MessageSegment.at(event.user_id)+MessageSegment.text('是，是新的冒险者大人！欢迎您来到昼光部队！希望您能在这里度过一段愉快的冒险时光....!'))
    await voicHandler(bot,event,"薇尔莉特","是，是新的冒险者大人！欢迎您来到昼光部队！希望您能在这里度过一段愉快的冒险时光....!")
    await join.finish(MessageSegment.text('我是这里的女佣薇尔莉特·奈奇，您有什么需要帮助的都可以呼唤我~让我们愉快地相处吧！'))
    await voicHandler(bot,event,"薇尔莉特","我是这里的女佣薇尔莉特·奈奇，您有什么需要帮助的都可以呼唤我~让我们愉快地相处吧！")

import nonebot
from nonebot import require
from nonebot_plugin_apscheduler import scheduler

def whichPVP():
   d1 = '2023-05-07'
   d2 = date.today()
  ######## 法1
  # （1）先将字符串-->时间格式date
   date1 = dt.datetime.strptime(d1, "%Y-%m-%d").date()  ##datetime.date(2018, 1, 6)
   date2 = d2
  # （2）计算两个日期date的天数差
   Days = (date2 - date1).days
   Days= Days % 4
   return Days
timing = require("nonebot_plugin_apscheduler").scheduler
@timing.scheduled_job("cron", hour='23', minute = '00' , second = '00' ,id="dingshi")
async def _():
    #这里是获取bot对象
    (bot,) = nonebot.get_bots().values()
    init_today()
    await bot.send_msg(
       message_type="group",
        group_id=855693189,
        message="每日好感度初始化完毕，记得参加仙人微彩"
    )
    a = whichpvp()
    if(a==1):
        bot.send_msg(
            message_type="group",
            group_id=855693189,
            message="今天是碎冰"
        )
    elif(a==2):
        bot.send_msg(
            message_type="group",
            group_id=855693189,
            message="今天是大草原"
        )
    elif(a==3):
        bot.send_msg(
            message_type="group",
            group_id=855693189,
            message="今天是阵地"

        )
    elif(a==0):
        bot.send_msg(
            message_type="group",
            group_id=855693189,
            message="今天是CF"
        )


######################################## date形式天数差



PVP=on_keyword(['今天PVP是'],priority=95,block=True)#亲昵昵称

@PVP.handle()
async def _(event: Event,bot:Bot):
       a=whichPVP()
       if (a == 1):
           await PVP.finish(Message("今天是碎冰"))
       elif (a == 2):
           await PVP.finish(Message("今天是大草原"))
       elif (a == 3):
           await PVP.finish(Message("今天是阵地"))
       elif (a == 0):
           await PVP.finish(Message("今天是CF"))

timingmaual=on_fullmatch("每日好感度初始化",permission=SUPERUSER,block=True,priority=1)
@timingmaual.handle()
async def _(event:PrivateMessageEvent):
   if(event.user_id==563944718):
    init_today()
    await timingmaual.finish(Message("每日好感度初始化完毕，记得参加仙人微彩"))

timing3 = require("nonebot_plugin_apscheduler").scheduler
@timing3.scheduled_job("cron", hour='10', minute = '30' , second = '30' ,id="dingshi3")
async def _():
    #这里是获取bot对象
    (bot,) = nonebot.get_bots().values()
    await bot.send_msg(
        message_type="private",
        user_id=750121182,
        message="早上好…愿愿小姐，昨晚睡得好吗？该起床了哦，早餐已经为您做好啦~"
    )




timing6 = require("nonebot_plugin_apscheduler").scheduler
@timing6.scheduled_job("cron", hour='21', minute = '35' , second = '30' ,id="dingshi6")
async def _():
    #这里是获取bot对象
    (bot,) = nonebot.get_bots().values()

    await bot.send_msg(
        message_type="group",
        group_id=855693189,
        message=f"[CQ:at,qq=all]各位冒险者大人好……！今天也要记得做蛮族任务哦。好友度升到满级之后可以拿到奖励坐骑呢~"
    )
    await bot.send_msg(
        message_type="private",
        user_id=750121182,
        message="愿愿小姐晚上好……！今天也要记得做蛮族任务哦？好友度升到满级之后可以拿到奖励坐骑呢~")

timing4 = require("nonebot_plugin_apscheduler").scheduler
@timing4.scheduled_job("cron", hour='12', minute = '34' , second = '35' ,id="dingshi4")
async def _():
    #这里是获取bot对象
    (bot,) = nonebot.get_bots().values()
    await bot.send_msg(
        message_type="private",
        user_id=750121182,
        message="中午好，不要勉强自己哦？愿愿小姐。"
    )
    await sleep(5)
    await bot.send_msg(
        message_type="private",
        user_id=750121182,
        message="随时都可以来找我贴贴...我很想念您！"
    )


timing5 = require("nonebot_plugin_apscheduler").scheduler
@timing5.scheduled_job("cron", hour='0', minute = '44' , second = '40' ,id="dingshi5")
async def _():
    #这里是获取bot对象
    (bot,) = nonebot.get_bots().values()
    await bot.send_msg(
        message_type="private",
        user_id=750121182,
        message="愿愿小姐，忙碌了一天一定很累吧？"
    )
    await sleep(5)
    await bot.send_msg(
        message_type="private",
        user_id=750121182,
        message="如果我可以帮您消除疲惫的话...（贴近）"
    )

if(platform.system()=="Windows"):
    data_dir = r"C:/Users/Administrator/first/src/plugins/decidebot/content"
elif(platform.system()=="Linux"):
    data_dir = "./data/favor/content"
else:
    data_dir = "./data/favor/content"


class Vividict(dict): #多层嵌套字典
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

def _decideText(Value:int,event,textstr:str): #输出语句
    value=int(Value)
    k=_checkValue(value,event)
    if (k==5):
        text=["请先使用（/注册好感度）注册好感度并阅读使用相关说明"]
        return text
    uid=event.user_id
    nickname=readName(str(uid))
    content=readDict(textstr)
    text=["1"]
    i=random.randint(1,len(content[str(k)]))
    j=0
    for key in content[str(k)][str(i)]:
        try:
            text[j]=str(content[str(k)][str(i)][key]).replace("某位",nickname)
        except IndexError:
            text.append(str(content[str(k)][str(i)][key]).replace("某位",nickname))
        j+=1
    return text

def _checkNegai(event):
    if(event.user_id in agree_list):
        return True
    else:
        return False

def _checkValue(value,event):
    if(_checkNegai(event)):
        return 4
    elif(value<=-300):
        return 5
    elif(value<100):
        return 1
    elif(value<400):
        return 2
    else:
        return 3

#对negai做出
def favor_dialog_rule2(event: GroupMessageEvent) -> bool: #触发器规则函数
    tem_jud=False
    all_list=trigger_text_2
    is_tme="[CQ:at,qq=750121182]" in event.raw_message
    for items in range(0,len(all_list)):
        if(all_list[items] in event.raw_message):
            tem_jud=True
    return (tem_jud and is_tme)

#对iki做出
def favor_dialog_rule(event: GroupMessageEvent) -> bool: #触发器规则函数
    tem_jud=False
    all_list=trigger_text_1+trigger_text_2
    is_tme="[CQ:at,qq=2656432337]" in event.raw_message
    for items in range(0,len(all_list)):
        if(all_list[items] in event.raw_message):
            tem_jud=True
    return (tem_jud and is_tme)

def ergodic_list(list_name: List[str],msg: str) -> bool: #遍历名为list_name的字符串列表判断msg是否在里面
    result=False
    try:
        length=len(list_name)
    except NameError:
        return False
    for items in range(0,length):
        if(list_name[items] in msg):
            result=True
    return result



def readDict(text):
    text=text+".json"
    content=Vividict()
    with open(data_dir+text, "r",encoding="utf-8") as f:
        content = json.load(f)
    return content
##基础功能实现##


def _checker(event: MessageEvent) -> bool:
    return (event.message_type=="private")


import datetime
from nonebot.rule import to_me


def favor_time(event:MessageEvent ) -> bool: #触发器规则函数
    if(event.message_type=="group"):
      now = datetime.datetime.now()
      current_hour = now.hour
      if current_hour >= 8 and current_hour <= 9:
        return True
    return False


def favor_time2(event:MessageEvent) -> bool: #触发器规则函数
    if(event.message_type=="private"):
      now = datetime.datetime.now()
      current_hour = now.hour
      if current_hour >= 8 and current_hour <= 9:
        return True
    else:
        return False

async def sendForMessageNoVoice(event: MessageEvent,bot:Bot,text):
    uid=event.user_id
    isfirst=True
    if(event.message_type=="private"):
        for temp in text:
            print(temp)
            if(isfirst):
                await bot.send_msg(
                    message_type="private",
                    user_id=uid,
                    message=temp)
                isfirst=False
                await sleep(2)
            else:
                await bot.send_msg(
                    message_type="private",
                    user_id=uid,
                    message=temp)
                await sleep(2)
    else:
        gid=int(event.group_id)
        for temp in text:
            print(gid)
            if(isfirst):
                await bot.send_msg(
                    message_type="group",
                    group_id=gid,
                    message=f"[CQ:at,qq={event.user_id}]"+temp)
                await sleep(2)
                isfirst=False
            else:
                await bot.send_msg(
                    message_type="group",
                    group_id=gid,
                    message=temp)
                await sleep(2)

async def sendForMessage(event: MessageEvent,bot:Bot,text):
    uid=event.user_id
    isfirst=True
    if(event.message_type=="private"):
        for temp in text:
            print(temp)
            if(isfirst):
                await bot.send_msg(
                    message_type="private",
                    user_id=uid,
                    message=temp)
                await voicHandler(bot,event,"薇尔莉特",temp)
                isfirst=False
            else:
                await bot.send_msg(
                    message_type="private",
                    user_id=uid,
                    message=temp)
                await voicHandler(bot,event,"薇尔莉特",temp)
    else:
        gid=int(event.group_id)
        for temp in text:
            print(gid)
            if(isfirst):
                await bot.send_msg(
                    message_type="group",
                    group_id=gid,
                    message=f"[CQ:at,qq={event.user_id}]"+temp)
                await voicHandler(bot,event,"薇尔莉特",temp)
                isfirst=False
            else:
                await bot.send_msg(
                    message_type="group",
                    group_id=gid,
                    message=temp)
                await voicHandler(bot,event,"薇尔莉特",temp)

nekosleep=on_startswith('',priority=10,rule=favor_time)
ask=on_startswith(['薇尔莉特','薇薇安','猫猫','小猫','在吗'],priority=100,block=True)#呼出
nick=on_keyword(['宝宝','宝贝','小宝','小猫咪','小咪',"老婆","小母猫"],priority=95,block=True,rule=to_me())#亲昵昵称
hello=on_keyword(['你好','您好','贵安','晚上好','下午好','中午好','午安'],priority=50,block=True)
askMorning=on_fullmatch(['早安','早上好','おはよう'],priority=50,block=True)
query=on_fullmatch(['薇尔莉特，你对我怎么看？','薇尔莉特 你对我怎么看？','薇薇安 你对我怎么看？','薇薇安，你对我怎么看？'],priority=50,block=True)#询问好感度
setname=on_regex(r"^/请叫我\s",priority=10,block=True)
night=on_fullmatch(['晚安','好梦'],priority=50,block=True)#晚安
reset=on_command("计数清零",priority=90,block=False,permission=SUPERUSER)
set=on_command("设置好感度",priority=50,block=False,permission=SUPERUSER)
help=on_command("好感度帮助",priority=50,block=True)
register=on_command("注册好感度",priority=49,block=False)
rank=on_command("好感度排名",priority=50,block=False)
uanswer=on_fullmatch(['怎么不理我'],priority=10,block=True)
think=on_keyword(['好想你','想你','思念你','想念'],priority=50,block=True)
tried=on_keyword(['好累','累','累死了','疲惫','崩溃','好烦','烦死','很烦'],priority=50,block=True)
away=on_keyword(['不要你了''你走吧''扔掉你''永别了',"讨厌你"],priority=50,block=True)
nekosleep2=on_startswith('',priority=1,rule=favor_time2)
nekosleep=on_startswith('',priority=2,rule=favor_time)
tirck=on_keyword(['俯首称臣',"权威","忤逆","扶手陈晨"],priority=20,block=True)#呼出



@nekosleep.handle()
async def _(matcher: Matcher,event:GroupMessageEvent):
    if(_checkNegai(event)):
        return
    if(event.to_me):
      await query.send(Message(f"呼…呼……嗯唔…"),at_sender=True)
      await query.send(Message("（她睡得很香…还是不要打扰她好了。）"))
      Matcher.stop_propagation(matcher)
    else:
        Matcher.stop_propagation(matcher)
        return
@nekosleep2.handle()
async def _(matcher: Matcher,event:PrivateMessageEvent):
    if(_checkNegai(event)):
        return
    await query.send(Message(f"呼…呼……嗯唔…"),at_sender=True)
    await query.send(Message("（她睡得很香…还是不要打扰她好了。）"))
    Matcher.stop_propagation(matcher)

#亲昵昵称
@nick.handle()
async def _(event: Event,bot:Bot):
    uid=str(event.user_id)
    value=readData(uid)
    text=_decideText(value,event,"nick")
    await sendForMessage(event,bot,text)

@hello.handle()
async def _(event: Event,bot:Bot):
    uid=str(event.user_id)
    value=readData(uid)
    text=_decideText(value,event,"hello")
    await sendForMessage(event,bot,text)

#呼出
@ask.handle()
async def _(event: Event,bot:Bot):
    uid=str(event.user_id)
    value=readData(uid)
    text=_decideText(value,event,"ask")
    await sendForMessage(event,bot,text)

@query.handle()
async def _(event: Event):
    uid=str(event.user_id)
    value=readData(uid)
    nickname=readName(uid)
    if(value>=-300):
        if(event.user_id  in agree_list):
            await query.send(Message(f"您…您是我一生中最重要的人！我愿意为您献上的一切…我什么都会为您做的！"),at_sender=True)
            await sleep(2)
        elif(value<100):
             await query.send(Message(f"诶…嗯，我还不太了解{nickname}大人呢……"),at_sender=True)
             await sleep(2)
        elif(value<400):
             await query.send(Message(f"[{nickname}大人是…很好的朋友，不是吗？跟您度过的时间真的很开心！"),at_sender=True)
             await sleep(2)
        else :
             await query.send(Message(f"诶？咦？怎、怎么突然问起这个……嗯，那个，就是…嗯嗯……"),at_sender=True)
             await sleep(2)
             await query.send(Message("只要是我能帮到您的我一定会全力以赴的……！"))
             await sleep(2)
        await query.finish(f"（薇尔莉特对您的好感度为{value}）!")
        #await query.finish(Message(f"[CQ:at,qq={event.user_user_idid}]紫息对你的好感度为{value}呀!{text(int(value))}"))
    else:
        await query.finish(Message(f"还没有注册好感度啊!输入/注册好感度 后才可以使用好感度系统!"),at_sender=True)

@uanswer.handle()
async def _(event: Event,bot:Bot):
    uid= str(event.user_id)
    value=readData(uid)
    text=_decideText(value,event,"uanswer")
    await sendForMessageNoVoice(event,bot,text)

@think.handle()
async def _(event: Event,bot:Bot):
    uid= str(event.user_id)
    value=readData(uid)
    text=_decideText(value,event,"think")
    await sendForMessageNoVoice(event,bot,text)

@night.handle()
async def _(event: Event,bot:Bot):
    uid= str(event.user_id)
    value=readData(uid)
    text=_decideText(value,event,"night")
    await sendForMessage(event,bot,text)

@askMorning.handle()
async def _(event: Event,bot:Bot):
    uid= str(event.user_id)
    print(1)
    value=readData(uid)
    text=_decideText(value,event,"askMorning")
    await sendForMessage(event,bot,text)

@away.handle()
async def _(event: Event,bot:Bot):
    uid= str(event.user_id)
    value=readData(uid)
    text=_decideText(value,event,"away")
    await sendForMessageNoVoice(event,bot,text)

@reset.handle()
async def _(event: PrivateMessageEvent):
    if(event.user_id  in agree_list):
        init_today()
        await reset.finish("清零完成!")
    logger.warning("有人要篡改数据!")
    await reset.finish("没有权限啊!")

@set.handle()
async def _(event: PrivateMessageEvent,args: Message = CommandArg()):
    arg = args.extract_plain_text().split()
    if(len(arg)==2):
        if(event.user_id in agree_list):
            if(changeData(arg[0],"741726402",int(arg[1]))!=-1):
                await reset.finish("设置完成!")
            else:
                await reset.finish("请先注册该用户!")
        await reset.finish("没有权限啊!")
    await reset.finish()

@tirck.handle()
async def _(event: Event,bot:Bot):
    uid= str(event.user_id)
    value=readData(uid)
    text=_decideText(value,event,"trick")
    if(value<=300):
        addData(uid,-10);
    await sendForMessage(event,bot,text)


@help.handle()
async def _(event: Event):
    await help.send(Message(f"请先使用(/注册好感度)来注册好感度系统"),at_sender=True)
    await sleep(2)
    await help.send(Message(f"用户系统：使用【/请叫我+空格+您的名字】来让薇尔莉特认识您。"))
    await sleep(2)
    await help.send(Message(f"好感度系统：输入【薇尔莉特，你对我怎么看？】可以查看薇尔莉特对您的好感度。每天和薇尔莉特互动或者夸赞薇尔莉特都可以增加好感度（互动类操作需要@），有些行为可能会倒扣好感度，请您友善对待薇尔莉特。"))
    await sleep(2)
    await help.send(Message(f"签到系统:输入【我要参加仙人微彩】或者【签到】来进行每日签到和抽取金币。"))
    await sleep(2)
    await help.send(Message(f"道具系统：输入【刷新布告板】触发道具系统，金币可以用来换取道具，道具可以提高好感度，解锁更多对话。"))
    await sleep(2)
    await help.send(Message(f"人工智能系统：薇尔莉特接入了chatgpt3.5，可以使用AI绘画、语音生成等功能。如果您想要更加智能的对话，请使用/chat进行请求智能薇尔莉特的帮助。更多薇尔莉特的玩法请在群里和薇尔莉特互动的时候慢慢探索吧~祝您玩得愉快！"))
    await sleep(2)
    await help.send(Message(f"更多薇尔莉特的玩法请在群里和薇尔莉特互动的时候慢慢探索吧~祝您玩得愉快！"))
"""
@help.handle()
async def _(event: Event,args: Message = CommandArg()):
    arg = args.extract_plain_text().split()
    if(len(arg)==0):
        await help.finish(Message(f"[CQ:at,qq={event.user_id}]每天薇尔莉特或者夸夸薇尔莉特都可以增加好感度!有些行为可能会倒扣好感度的!"))
    elif(len(arg)==1):
        if(arg[0]=="抽奖"):
            await help.finish(Message(f"[CQ:at,qq={event.user_id}]抽奖系统:输入 我要参加仙人微彩 来进行抽取金币，道具系统暂未开放，好感度可以通过 我要参加仙人彩来换取金钱 每次消耗一定金币，每日都增加一次次数。"))
        else:
            await help.finish(Message("无效参数!"))
    else:
        await help.finish(Message("无效参数!"))
"""
@setname.handle()
async def _(event:Event):
    msg = event.get_plaintext()
    userInput: str =  re.sub(r"^/请叫我\s+", '', msg)
    uid=str(event.user_id)
    if (readData(uid)<=-300):
        await setname.finish(Message(f"还没有注册好感度啊!输入/注册好感度 后才可以使用好感度系统!"),at_sender=True)
    else:
        changeNickName(uid,userInput)
        if(_checkNegai(event)):
            await setname.finish(Message(f"好的 {userInput}大人"),at_sender=True)
        else:
            await setname.finish(Message(f"好、好的，如果您希望我这么叫您的话，那、{userInput}大人，贵安…"),at_sender=True)

@uanswer.handle()
async def _(event: Event,bot:Bot):
    uid= str(event.user_id)
    value=readData(uid)
    text=_decideText(value,event,"uanswer")
    await sendForMessage(event,bot,text)
@tried.handle()
async def _(event: Event,bot:Bot):
    uid= str(event.user_id)
    value=readData(uid)
    text=_decideText(value,event,"tried")
    await sendForMessage(event,bot,text)
    if (event.user_id==750121182):
        await eat.wtdp(event,bot)

@register.handle()
async def _(event:Event):
    uid=str(event.user_id)
    if (readData(uid)<=-300):
        initData(uid)
        initData_i(uid)
        await sendForMessage(event,bot,"很高兴认识您！某位大人。")
        await sleep(2)
        await help.send(Message(f"用户系统：使用【/请叫我+空格+您的名字】来让薇尔莉特认识您。"))
        await sleep(2)
        await help.send(Message(f"好感度系统：输入【薇尔莉特，你对我怎么看？】可以查看薇尔莉特对您的好感度。每天和薇尔莉特互动或者夸赞薇尔莉特都可以增加好感度（互动类操作需要@），有些行为可能会倒扣好感度，请您友善对待薇尔莉特。"))
        await sleep(2)
        await help.send(Message(f"签到系统:输入【我要参加仙人微彩】或者【签到】来进行每日签到和抽取金币。"))
        await sleep(2)
        await help.send(Message(f"道具系统：输入【刷新布告板】触发道具系统，金币可以用来换取道具，道具可以提高好感度，解锁更多对话。"))
        await sleep(2)
        await help.send(Message(f"人工智能系统：薇尔莉特接入了chatgpt3.5，可以使用AI绘画、语音生成等功能。如果您想要更加智能的对话，请使用/chat进行请求智能薇尔莉特的帮助。更多薇尔莉特的玩法请在群里和薇尔莉特互动的时候慢慢探索吧~祝您玩得愉快！"))
        await sleep(2)
        await help.send(Message(f"更多薇尔莉特的玩法请在群里和薇尔莉特互动的时候慢慢探索吧~祝您玩得愉快！"))
    else:
        await register.finish(Message(f"真是的…您真爱说笑，我们不是已经认识过了吗！"),at_sender=True)

@rank.handle()
async def _(bot:Bot,event:GroupMessageEvent):
    json=raw_json()
    count=0
    msg=Message()
    bot = nonebot.get_bot()
    sort_json = sorted(json.items(), key=lambda x: x[1]["Status"]['Favor'], reverse=True)
    for keys,values in sort_json:
        if(count==8):
            break
        count+=1
        info=await bot.get_group_member_info(group_id=event.group_id,user_id=int(keys),no_cache=False)
        card=info.get("card")
        if(card==''):
            card=info.get("nickname")
        dict_new=values
        for i in dict_new.items():
            favor=i[1]["Favor"]
            msg+=Message(f"{count}.{card}(qq:{keys}):{favor}\n")
    if(message!= ""):
        await rank.finish(msg)
    else:
        await rank.finish("数据错误！")



inventory=on_fullmatch("打开背包",priority=50,block=False)
times_q=on_fullmatch("查询剩余次数",priority=50,block=False)
extract=on_fullmatch("我要参加仙人微彩",priority=50,block=True)
inventorymoney=on_fullmatch("打开钱包",priority=50,block=False)
sendpresent=on_regex(r"^送给薇尔莉特\s+\d+",priority=50,block=False)
sign=on_fullmatch("签到",priority=3,block=False)



@inventory.handle()
async def _(event: Event):
    uid=str(event.user_id)
    lst=get_item_list(uid)
    nickname=readName(uid)
    msg=f"{nickname}大人，您的背包里有\n"
    if(lst==-1):
        await inventory.finish(MessageSegment.at(event.user_id)+Message(f"{nickname}大人，背包里没有物品!"))
    else:
        for j in lst.keys():
            numb=lst[str(j)]["number"]
            name=getItemName(j)
            msg+=f"{name},编号:{j},数量:{numb}\n"
    print(msg)
    await inventory.finish(Message(msg),at_sender=True)

@sendpresent.handle()
async def _(event: Event):
    msg = event.get_plaintext()
    msg = re.sub(r"^送给薇尔莉特\s+", '', msg)
    uid=str(event.user_id)
    item=getItemDetail(msg)
    if(item==""):
        await sendpresent.finish(Message(f"输入错误！！"),at_sender=True)
    effectId=item["EffectId"]
    lst=get_item_list(uid)
    nickName=readName(uid)
    ItemName=getItemName(msg)
    print(ItemName)
    try:#判断是否有这个物品
        lst[msg]["number"]
    except KeyError as b:
        await sendpresent.finish(Message(f"咦…？包包里没有您说的这个物品呀…"),at_sender=True)
    if(effectId!=0):
        await sendpresent.finish(Message(f"{ItemName}还不能够赠送！！"),at_sender=True)
    add_item(uid,msg,-1)
    text=getItemDialogue(msg,nickName)
    addTargetData(uid,"Favor",getItemFavor(msg))
    for j in range(0,len(text)):
       if(j==0):
          await favor_trigger.send(Message(text[j]),at_sender=True)
          await sleep(2)
       else:
          await favor_trigger.send(Message(text[j]))
          if(j<len(text)-1):
             await sleep(2)

@inventorymoney.handle()
async def _(event: Event):
    uid=str(event.user_id)
    money=readTargetData(uid,"Money")
    await inventorymoney.finish(Message(f"的钱包里有{money}金币"),at_sender=True)

@extract.handle()
async def _(event: Event):
    uid=str(event.user_id)
    if(readTargetData(uid,"Extra")<=0):
        await extract.finish(Message("今日的抽奖次数已经用完了哦!"),at_sender=True)
    i=random.randint(10,100)
    if(i==100 or i==75 ):
        addTargetData(uid, "Extra", -1)
        await extract.finish(Message("恭喜您获得了0金币"),at_sender=True)
    else:
        addTargetData(uid,"Extra",-1)
        addTargetData(uid,'Money',i)
        await extract.finish(Message(f"恭喜您获得了{i}金币"),at_sender=True)

@sign.handle()
async def _(event: Event):
    uid=str(event.user_id)
    nickname=readName(uid)
    if(readDayData(uid,"Yesterday")==0):
        changeDayDataOnce(uid)
        Consign=readDayData(uid,"ConSign")
        allsign=readDayData(uid,"All")
        monthSign=readDayData(uid,"Month")
        i=random.randint(10,100)
        addTargetData(uid,'Money',i)
        b=int(Consign/10)+5
        addData(uid,b)
        money=readTargetData(uid,"Money")
        msg=f"签到成功，{nickname}大人，这是签到奖励：{i}金币\n"+f"已经连续签到了{Consign}天\n"+f"本月签到了{monthSign}天\n"+f"总共签到了{allsign}天\n"+f""+f"钱包里有{money}元\n"
        await sign.send(Message(msg),at_sender=True)
    else:
        await sign.finish(Message(f"{nickname}大人，今天已经签到过了"),at_sender=True)

'''
@gungle.handle()
async def _(event: Event):
    uid=str(event.user_id)
    favor=readData(uid)
    money=readTargetData(uid,"Money")
    if(favor<=0):
        await gungle.send(Message("对不起……我还不可以去帮您买仙人彩呢!"),at_sender=True)
        await gungle.finish(Message("（好感度不够）"))
    if(money<=int(50-int(0.03*favor))):
        await gungle.finish(Message("对不起……我还不可以去帮您买仙人彩呢!"),at_sender=True)
        await gungle.finish(Message("（金币不够）"))
    i=random.randint(1,10000)
    i=i+int(2*favor)
    addTargetData(uid,'Favor',120)
    addTargetData(uid,'Money',-50+int(0.03*favor))
    if(i<500):
        addTargetData(uid,'Money',-200)
        await gungle.finish(Message(f"您roll到了{i}，恭喜再倒输200金币"),at_sender=True)
    if(i<1500):
        addTargetData(uid,'Money',-100)
        await gungle.finish(Message(f"您roll到了{i}，恭喜再倒输100金币"),at_sender=True)
    if(i<2000):
        addTargetData(uid,'Money',-50)
        await gungle.finish(Message(f"您roll到了{i}，恭喜再倒输50金币"),at_sender=True)
    if(i<3000):
        addTargetData(uid,'Money',10)
        await gungle.finish(Message(f"您roll到了{i}，恭喜您赢了10金币"),at_sender=True)
    if(i<3500):
        addTargetData(uid,'Money',30)
        await gungle.finish(Message(f"您roll到了{i}，恭喜您赢了50金币"),at_sender=True)
    if(i<4500):
        addTargetData(uid,'Money',80)
        await gungle.finish(Message(f"您roll到了{i}，恭喜您赢80金币"),at_sender=True)
    if(i==5639):
        addTargetData(uid,'Money',2000)
        await gungle.finish(Message(f"您roll到了{i}，恭喜您赢了1000金币"),at_sender=True)
    if(i<5700):
        addTargetData(uid,'Money',100)
        await gungle.finish(Message(f"您roll到了{i}，恭喜您赢了100金币"),at_sender=True)
    if(i==7502):
        addTargetData(uid,'Money',7502)
        await gungle.finish(Message(f"您roll到了{i}，恭喜您赢了7502金币"),at_sender=True)
    if(i<7600):
        addTargetData(uid,'Money',150)
        await gungle.finish(Message(f"您roll到了{i}，恭喜您赢了150金币"),at_sender=True)
    if(i<10000):
        addTargetData(uid,'Money',200)
        await gungle.finish(Message(f"您roll到了{i}，恭喜您赢了200金币"),at_sender=True)
    else:
        addTargetData(uid,'Money',300)
        await extract.finish(Message(f"您roll到了{i}，恭喜您赢了300金币"),at_sender=True)
'''
@times_q.handle()
async def _(event: GroupMessageEvent):
    uid=str(event.user_id)
    value=readTargetData(uid,"extra")
    await times_q.finish(MessageSegment.at(event.user_id)+Message(f"次数剩余:{value}"))

##紫息每日心情

def _checker1(event: GroupMessageEvent) ->bool :
    return (event.message_type=="group")

mood_d=on_keyword({"薇尔莉特今天心情怎么样"},rule=_checker1,priority=98)

def mood_text(mood: int):
    if(mood<=20):
        return "薇尔莉特今天不开心!不要惹薇尔莉特生气!"
    elif(mood<=40):
        return "薇尔莉特今天心情不太好......"
    elif(mood<=60):
        return "薇尔莉特今天棒棒哒~"
    elif(mood<=80):
        return "薇尔莉特想要一起玩!"
    elif(mood<=100):
        return "薇尔莉特今天好开心呀!!!"

@mood_d.handle()
async def _():
    mood=mood_daliy()
    logger.info(f"今日心情值:{mood_daliy()}")
    await mood_d.finish(Message(f"{mood_text(mood)}"))


##提升好感度 法二##
#此方法需要 @紫息


trigger_text_1=["贴贴","抱抱","抱一下"]
trigger_text_2=["屁股"]
trigger_text_3=["亲亲","亲吻","亲一个","kiss","吻","啾啾","啾咪","啵啵"]
trigger_text_4=["可爱","厉害","漂亮","好棒","聪明","美丽","好看","最棒"]
trigger_text_5=["笨蛋","傻瓜","笨猫","笨","傻"]
trigger_text_6=["摸摸","摸头","抚摸"]
trigger_text_7=["喜欢你","爱你"]

def _decideText2(Value:int,event,textstr:str,list): #输出语句
    value=int(Value)
    k=_checkValue(value,event)
    if (k==5):
        text=["请先使用（/注册好感度）注册好感度并阅读使用相关说明"]
        return text
    uid=str(event.user_id)
    addData(uid,list[k-1])
    nickname=readName(str(uid))
    content=readDict(textstr)
    text=['1']
    i=random.randint(1,len(content[str(k)]))
    j=0
    for key in content[str(k)][str(i)]:
        try:
            text[j]=str(content[str(k)][str(i)][key]).replace("某位",nickname)
        except IndexError:
            text.append(str(content[str(k)][str(i)][key]).replace("某位",nickname))
        j+=1
    return text

#对negai做出
def favor_dialog_rule2(event: GroupMessageEvent) -> bool: #触发器规则函数
    tem_jud=False
    all_list=trigger_text_2
    is_tnegai="[CQ:at,qq=750121182]" in event.raw_message
    is_tme="[CQ:at,qq=2656432337]" in event.raw_message
    for items in range(0,len(all_list)):
        if all_list[items] in event.raw_message:
            tem_jud=True
    return (tem_jud and (is_tme or is_tnegai))

#对iki做出
def favor_dialog_rule(event: Event) -> bool: #触发器规则函数
    tem_jud=False
    all_list=trigger_text_1+trigger_text_2+trigger_text_3+trigger_text_4+trigger_text_5+trigger_text_6+trigger_text_7
    is_tme="[CQ:at,qq=2656432337]" in event.raw_message
    for items in range(0,len(all_list)):
        if(all_list[items] in event.raw_message):
            tem_jud=True
    if(event.message_type=="group"):
        return (tem_jud and is_tme)
    elif(event.message_type=="private"):
        print(1)
        return tem_jud

favor_trigger=on_message(favor_dialog_rule,priority=30,block=True)

list=[0,1,2,3]
list1=[-3,-2,-1,5]
list2=[0,0,1,1]
list3=[4,3,2,2]
list4=[-1,-1,0,2]
list5=[2,2,1,2]
list6=[2,2,1,2]

@favor_trigger.handle()
async def _(event: Event,bot:Bot):
    uid=str(event.user_id)
    message=re.sub(u"\\[.*?]", "", event.raw_message) #提取原始消息并去除CQ消息段
    value=readData(uid)
    if(value>=-300):
        logger.info(f"{event.raw_message}")
        if(ergodic_list(trigger_text_1,message)):
           value=readData(uid)
           text=_decideText2(value,event,"hug",list)
           await sendForMessageNoVoice(event,bot,text)
        if(ergodic_list(trigger_text_2,message)):
            value=readData(uid)
            text=_decideText2(value,event,"pigu",list1)
            await sendForMessageNoVoice(event,bot,text)
        if(ergodic_list(trigger_text_3,message)):#亲亲
            value=readData(uid)
            text=_decideText2(value,event,"kiss",list2)
            await sendForMessageNoVoice(event,bot,text)
        elif(ergodic_list(trigger_text_4,message)):
            value=readData(uid)
            text=_decideText2(value,event,"good",list3)
            await sendForMessage(event,bot,text)
        elif(ergodic_list(trigger_text_5,message)):
            value=readData(uid)
            text=_decideText2(value,event,"lovelove",list4)
            await sendForMessageNoVoice(event,bot,text)
        elif(ergodic_list(trigger_text_6,message)):
            value=readData(uid)
            text=_decideText2(value,event,"touch",list5)
            await sendForMessageNoVoice(event,bot,text)
        elif(ergodic_list(trigger_text_7,message)):
            value=readData(uid)
            text=_decideText2(value,event,"love",list6)
            await sendForMessageNoVoice(event,bot,text)
    else:
        await favor_trigger.finish(Message("请先注册好感度!"))

#%%
