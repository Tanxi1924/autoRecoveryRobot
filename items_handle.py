# Python Script Created by MRS
import json
import os
import platform
import random
from datetime import date

from nonebot.log import logger




class Vividict(dict): #多层嵌套字典
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

if(platform.system()=="Windows"):
    data_dir = r"C:/Users/Administrator/first/src/plugins/decidebot/"
elif(platform.system()=="Linux"):
    data_dir = "./data/favor"
else:
    data_dir = "./data/favor"

def initData_i(uid: str): #背包
    data=Vividict()
    data[uid]={}
    with open(data_dir + "bag.json", "r",encoding="utf-8") as f:
        content = json.load(f)
    content.update(data)
    with open(data_dir + "bag.json", 'w',encoding="utf-8") as f_new:
        json.dump(content,f_new,indent=4)

def get_item_list(uid: str):
    with open(data_dir + "bag.json", "r",encoding="utf-8") as f:
        content = json.load(f)
    items=content[uid]
    if(items=={}):
        return -1
    else:
        return items

def add_item(uid: str,itemid:str,num: int):
    if(itemid=="-1") :
        return -1
    with open(data_dir + "bag.json", "r",encoding="utf-8") as f:
        content = json.load(f)
    bear2={itemid:{"number":num}}
    try:
        logger.info(f"{int(itemid)}的好感度增加了{num}!")
        content[uid][itemid]["number"]+=num
        if(content[uid][itemid]["number"]<=0):
            content[uid].pop(itemid)
    except KeyError:
        print(1);
        if(num>0):
            content[uid][itemid]={"number":num}
        else:
            return -1
    with open(data_dir + "bag.json", 'w',encoding="utf-8") as f_new:
        json.dump(content,f_new,indent=4)

'''
def add_item_num(uid: str,item: dict,num: int):   # 增加物品数量
    global name
    lst=get_item_list(uid)
    if(lst!=-1):
        for i in item.keys():
            name=i
            break
        for keys in lst:
            if(name==keys):
                with open(data_dir + "bag.json", "r", encoding="utf-8") as f:
                    content = json.load(f)
                if (content[uid][name]["number"] + num <= 0):
                    content[uid].pop(name)
                else:
                    content[uid][name]["number"] += num
                with open(data_dir + "bag.json", 'w', encoding="utf-8") as f_new:
                    json.dump(content, f_new, indent=4)
                return
        add_item(uid,item)
    else:
        add_item(uid, item)
        return
'''
itemRandomlist=[0,0]

def createrandom_item(level: int=0): #随机抽取物品
    with open(data_dir + "item.json", "r",encoding="utf-8") as f:
        content = json.load(f)
    j=0
    global itemRandomlist
    for key in content :
        max=int(content[key]["Status"]['Probability'])#千分的概率
        for i in range(1,max+1):
            try:
                itemRandomlist[j]=int(key)

            except IndexError:
                itemRandomlist.append(int(key))
            j+=1
    print(itemRandomlist[1])

def RandomItem():
    global itemRandomlist
    if(itemRandomlist[0]==0):
        createrandom_item()
    i=random.randint(0,999)
    try:
        print(itemRandomlist[i])
        return itemRandomlist[i]
    except IndexError:
        return 0

def init(itemid):
    with open(data_dir + "item.json", "r",encoding="utf-8") as f:
        content = json.load(f)
    content[itemid]["Status"]={"ItemName":"","Money":0,"Description":"","Probability":0,"Favor":0,"Effertid":0}
    with open(data_dir + "item.json", 'w',encoding="utf-8") as f_new:
        json.dump(content,f_new,indent=4)

def getItemDetail(itemid:str):
    with open(data_dir + "item.json", "r",encoding="utf-8") as f:
        content = json.load(f)
    try:
       temp=content[str(itemid)]["Status"]
       return temp
    except KeyError :
        return ""


def getItemMoney(itemid:str)-> int:
    with open(data_dir + "item.json", "r",encoding="utf-8") as f:
        content = json.load(f)
    return content[str(itemid)]["Status"]["Money"]

def getItemFavor(itemid:str)-> int:
    with open(data_dir + "item.json", "r",encoding="utf-8") as f:
        content = json.load(f)
    return int(content[str(itemid)]["Status"]["Favor"])

def getItemName(itemid:str)-> str:
    with open(data_dir + "item.json", "r",encoding="utf-8") as f:
        content = json.load(f)
    return content[str(itemid)]["Status"]["ItemName"]

def getItemDialogue(itemid:str,nickname:str):
    with open(data_dir + "item.json", "r",encoding="utf-8") as f:
        content = json.load(f)

    print(itemid)
    text=["",""]
    j=0
    print(content[str(itemid)]["Dialogue"])
    for key in content[str(itemid)]["Dialogue"] :
        try:
            text[j]=str(content[str(itemid)]["Dialogue"][key]).replace("某位",nickname)
        except IndexError:
            text.append(str(content[str(itemid)]["Dialogue"][key]).replace("某位",nickname))
        j+=1
    print(text)
    return text

if __name__ == "__main__":
    # pass
    createrandom_item()

    print()
    # print(lst[0])
    # for keys in content:
    #     initData_i(keys)