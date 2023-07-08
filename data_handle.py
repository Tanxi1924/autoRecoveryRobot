import json
import os
import platform
import random
import operator
from datetime import date
from .items_handle import *

from nonebot.log import logger
# from .items_handle import initData_i


class Vividict(dict): #多层嵌套字典
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

# scheduler = require("nonebot_plugin_apscheduler").scheduler

if(platform.system()=="Windows"):
    data_dir = r"C:/Users/Administrator/first/src/plugins/decidebot/"
elif(platform.system()=="Linux"):
    data_dir = "./data/favor"
else:
    data_dir = "./data/favor"

def raw_json():
    with open(data_dir + "favor.json", "r",encoding="utf-8") as f:
        content = json.load(f)
    return content

def raw_jsonw(content):
    with open(data_dir + "favor.json", 'w',encoding="utf-8") as f_new:
        json.dump(content, f_new, indent=4)

def addNewType(uid: str,type: str): #添加Status类型
    with open(data_dir + "favor.json","r",encoding="utf-8") as f:
        content = json.load(f)
    content[uid]["Status"].update({f"{type}":0})
    with open(data_dir + "favor.json", 'w',encoding="utf-8") as f_new:
        json.dump(content, f_new, indent=4)

def addNewType(uid: str,type2: str,type: str): #添加新数据类型
    with open(data_dir + "favor.json","r",encoding="utf-8") as f:
        content = json.load(f)
    content[uid][type2].update({f"{type}":0})
    with open(data_dir + "favor.json", 'w',encoding="utf-8") as f_new:
        json.dump(content, f_new, indent=4)

def initData(uid: str): #初始化人物存档
    data=Vividict()
    data[uid]["Status"]={"Favor":0,"NickName":"冒险者","Today":0,"Money":0,"Extra":1,"RMoney":0,"Refresh":3,}
    data[uid]["ShoppingList"]={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,"12":0,"13":0}
    data[uid]["DayStatus"]={"ConSign":0,"Yesterday":0,"Month":0,"All":0}
    # addNewType(uid,"Favor") #好感度
    # addNewType(uid, "Today") #今日好感度增加量
    # addNewType(uid, "DialogAdd") #对话好感度增加量
    with open(data_dir + "favor.json", "r",encoding="utf-8") as f:
        content = json.load(f)
    content.update(data)
    with open(data_dir + "favor.json", 'w',encoding="utf-8") as f_new:
        json.dump(content,f_new,indent=4)
        f_new.close()

def init_today(): #初始化每日数值
    with open(data_dir + "favor.json", "r",encoding="utf-8") as f:
        content = json.load(f)
    for keys,values in content.items():
        values["Status"]["Today"] = 0
        values["Status"]["Extra"] = 1
        values["Status"]["Refresh"] = 3
        try:
         if(values["DayStatus"]["Yesterday"]==0):
            values["DayStatus"]["ConSign"]=0
         values["DayStatus"]["Yesterday"]=0
        except KeyError:
            print(values)
    with open(data_dir + "favor.json", 'w',encoding="utf-8") as f_new:
        json.dump(content, f_new, indent=4)

def readDayData(uid: str,type:str): #读取日常示数
    with open(data_dir + "favor.json", "r",encoding="utf-8") as f:
        content = json.load(f)
    try:
        value=content[uid]["DayStatus"][type]
        return int(value)
    except KeyError:
        return -1


def changeDayDataOnce(uid: str): #读取好感度示数
    with open(data_dir + "favor.json", "r",encoding="utf-8") as f:
        content = json.load(f)
    try:
        content[uid]["DayStatus"]["Yesterday"]=1
        content[uid]["DayStatus"]["All"]+=1
        content[uid]["DayStatus"]["Month"]+=1
        content[uid]["DayStatus"]["ConSign"]+=1
        with open(data_dir + "favor.json", 'w',encoding="utf-8") as f_new:
            json.dump(content, f_new, indent=4)
    except KeyError:
        return -1

def changeDayData(uid: str,type:str,value:int): #读取好感度示数
    with open(data_dir + "favor.json", "r",encoding="utf-8") as f:
        content = json.load(f)
    try:
        content[uid]["DayStatus"][type]=value
        logger.info(f"{int(uid)}的{type}增加了{value}!!!")
        return int(value)
    except KeyError:
        return -1

def changeData(uid: str,favor: int): #修改好感度
    with open(data_dir + "favor.json", "r",encoding="utf-8") as f:
        content = json.load(f)
        try:
            content[uid]["Status"]["Favor"]=favor
            with open(data_dir + "favor.json", 'w',encoding="utf-8") as f_new:
                json.dump(content,f_new,indent=4)
        except KeyError:
            return -1

def changeTargetData(uid: str,type: str,value: int): #修改指定数值
    with open(data_dir + "favor.json", "r",encoding="utf-8") as f:
        content = json.load(f)
        try:
            content[uid]["Status"][f"{type}"]=value
            with open(data_dir + "favor.json", 'w',encoding="utf-8") as f_new:
                json.dump(content,f_new,indent=4,)
        except KeyError:
            return -1

def changeNickName(uid: str,value: str): #修改指定数值
    with open(data_dir + "favor.json", "r",encoding="utf-8") as f:
        content = json.load(f)
        try:
            content[uid]["Status"]['NickName']=value
            with open(data_dir + "favor.json", 'w',encoding="utf-8") as f_new:
                json.dump(content,f_new,indent=4,)
        except KeyError:
            return -1

def readData(uid: str) -> int : #读取好感度
    with open(data_dir + "favor.json", "r",encoding="utf-8") as f:
        content = json.load(f)
    try:
        value=content[uid]["Status"]["Favor"]
        return int(value)
    except KeyError:
        return -1100

def readName(uid: str) -> str : #读取名字
    with open(data_dir + "favor.json", "r",encoding="utf-8") as f:
        content = json.load(f)
    try:
        value=content[uid]["Status"]["NickName"]
        return value
    except KeyError:
        return "冒险者"

def readMaxData(uid: str) -> int : #读取今日变化好感度
    with open(data_dir + "favor.json", "r",encoding="utf-8") as f:
        content = json.load(f)
    try:
        return int(content[uid]["Status"]["Today"])
    except KeyError:
        return -114514

def readTargetData(uid: str,type: str) -> int: #读取指定类型数据
    with open(data_dir + "favor.json", "r",encoding="utf-8") as f:
        content = json.load(f)
    try:
        return int(content[uid]["Status"][f"{type}"])
    except KeyError:
        return -1

def addData(uid: str,favor: int): #增加好感度
    value=readMaxData(uid)
    if(value!=-114514):
        value+=favor
        if (value <= 20):
            if(readData(uid)+favor>-200 and readData(uid)+favor<1000):
                with open(data_dir + "favor.json", "r",encoding="utf-8") as f:
                    content = json.load(f)
                content[uid]["Status"]["Favor"] += favor
                content[uid]["Status"]["Today"] += favor
                with open(data_dir + "favor.json", 'w',encoding="utf-8") as f_new:
                    json.dump(content, f_new, indent=4)
                logger.info(f"{int(uid)}的好感度增加了{favor}!")
            else:
                logger.warning(f"{int(uid)}的好感度已经超出范围!")
        else:
            logger.warning(f"{int(uid)}今日好感度增加量已到达上限!")
    else:
        return -1

def addTargetData(uid: str,type: str,value: int): #增加某项Status
    try:
        with open(data_dir + "favor.json", "r",encoding="utf-8") as f:
            content = json.load(f)
        content[uid]["Status"][f"{type}"] += value
        with open(data_dir + "favor.json", 'w',encoding="utf-8") as f_new:
            json.dump(content, f_new, indent=4)
        logger.info(f"{int(uid)}的{type}增加了{value}!!!")
    except KeyError:
        return -1

def randomDataChange(uid: str,type: int): #好感度随机变化
    """
    随机更改好感度
    uid:群组ID
    type:随机数类型
    """
    if(type==0):
        choice=random.randint(-2,4)
    elif(type==1):
        choice=random.randint(-3,1)
    elif (type == 2):
        choice = random.randint(-3, 0)
    elif(type==3):
        choice=random.randint(0,3)
    else:
        choice = random.randint(-3, 3)
    addData(uid,choice)

def mood_daliy(): #每日心情基值
    rnd = random.Random()
    seed = int(date.today().strftime("%y%m%d"))
    rnd.seed(seed)
    mood=int(rnd.gauss(60,50))
    while(mood<0 or mood>100):
        mood = int(rnd.gauss(60, 50))
    # mood=rnd.randint(0,100)
    return mood

def createShoppingList(uid:str):
    with open(data_dir + "favor.json", "r",encoding="utf-8") as f:
        content = json.load(f)
    favor=readData(uid)
    shoppinglist=list()
    maxrange=int((favor)/300)
    maxrange+=5
    print(maxrange)
    for i in range(1,maxrange):
        j=RandomItem()
        if(j!=-1):
           shoppinglist.append(RandomItem())
    print(shoppinglist)
    if(len(shoppinglist) == 0):
        shoppinglist.append(2)
    print(len(shoppinglist))
    for i in range(1,len(shoppinglist)+1):
       content[uid]["ShoppingList"][str(i)]=shoppinglist[i-1]
    with open(data_dir + "favor.json", 'w',encoding="utf-8") as f_new:
        json.dump(content, f_new, indent=4)

def getShoppingList(uid:str):
    with open(data_dir + "favor.json", "r",encoding="utf-8") as f:
        content = json.load(f)
    shoppingDict=dict()
    ShoppingList=list()
    content[uid]["ShoppingList"]
    for i in range (1,13): #修改物品列表的时候要修改数字
        values=content[uid]["ShoppingList"][str(i)]
        if(values!=0):
            ShoppingList.append(int(values))
    print(ShoppingList)
    return ShoppingList

def setShoppingList(uid:str,id:int):
    with open(data_dir + "favor.json", "r",encoding="utf-8") as f:
        content = json.load(f)
    content[uid]["ShoppingList"]
    content[uid]["ShoppingList"][str(id)]=0
    with open(data_dir + "favor.json", 'w',encoding="utf-8") as f_new:
        json.dump(content, f_new, indent=4)



def _changeNick(text:str,nickname:str):
    print(text)
    text.replace("xxxx", nickname)
    return text
if __name__=="__main__":
    # pass
    #  #addNewType("3237231778","684869122","DialogMax")
    #  #print(readTargetData("3237231778","684869122","DialogMax"))
    #    initData("3237","741726402",0)
    #    initData("114514","741726402",0)
    initData("563944718")
    #     addData("32372317780","741726402",3)
    #      addData("3237","741726402",3)
    #     init_today()
#    readName('563944718')
    #      json_data=raw_json()
    #     sort_json=sorted(json_data.items(),key=lambda x:x[1]["741726402"]['Favor'],reverse=True)
    #     for keys,values in sort_json:
    #          print(keys)
    #     a=readTargetData("3237231778", "741726402", "Extract")
    #     with open(data_dir + "favor.json", "r") as f:
    #        content = json.load(f)
    print(1)
    #    for items in content:
#      addNewType(items,"741726402","Extract")
#%%

#%%
