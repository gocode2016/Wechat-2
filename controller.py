# -*- coding: utf-8 -*-
# filename: controller.py

import json
import os
import time

class UserReader(object): #用户数据读写器
    def __init__(self, user): #读取构造[读结构]
        self.user = user
        if os.path.isfile("users/" + self.user + ".json"):
            file = "users/" + str(self.user)
            re_UserData = open(file, "r+")
            self.Data = json.loads(re_UserData.read)
            self.Read = True
            re_UserData.close()
        else:
            self.Read = False

    def register(self, key=False): #用户注册[读/写结构]
        key_file = open("config/apikey.json", "r+")
        api_key = json.loads(key_file.read())
        key_file.close()
        Name = False #为下面写入器打标记的
        NickName = None
        Status = "Main"
        Permission = {"AccountBook": False, "DevZone": False}
        if key:
            try:
                 if api_key[key][isUsed]: #key鉴权
                     raise MyException("This Api Key has been used: ",key)
                 NickName = api_key[key]["NickName"]
                 Permission = api_key[key]["Permission"]
                 Data.AccountBook = AccountBook_Socket(Permission[AccountBook]) #注意：传入的是要对应模块权限的布尔值
                Name = self.user
                callback = "Content.keyok"
            except expression as identifier:
                print "[Controller] UserRegister Callback: ", identifier
                return "Content.illegalkey"
        else:
            callback = "Content.onkeyok"
            Name = self.user

        if Name: #真正开始写入用户数据的部分
            while Name:
                try:
                    path = "users/" + Name
                    userfile = open(path,"w+")
                    writedata = {}
                    waitfordatakey = ["Name", "NickName", "Status"] #这里存放的是除字典以外的元素数据
                    waitfordata = [Name, NickName, Status]
                    # 由于Python 2不支持在列表中存放字典元素，因此包含字典数据的要分开处理
                    writedata["Permission"] = Permission
                    if Data.AccountBook: #如果未授权是返回False，如果变量不存在会出错
                        writedata["Data.AccountBook"] = Data.AccountBook

                    for key, data in zip(waitfordatakey,waitfordata): #将数据的键与值打包，并对应赋予完成绑定
                        writedata[key] = data

                    userfile.write(writedata)
                    userfile.close()
                    Name = False #循环标记，以离开循环

                except expression:
                    print "[Controller] Cannot write user data,try again"
                    time.sleep(0.1) #IO操作延时

        return callback


    def AccountBook_Socket(self, Permission):
        if Permission: #在此分支做模块功能鉴权
            data = {"Count":0, "TransferCount":0}
            return data
        else:
            return False

    def UserIO(self): #用户数据写入器[写结构]
        pass



class CallBackReader(object): #返回码解析对象，服务初始化时调用
    def __init__(self):
        file = open("config/callback.json", "r")
        self.Data = json.loads(file.read())
        file.close()
    

class ListReader(object): #菜单列表解析对象，服务初始化时调用
    def __init__(self):
        file = open("config/list.json", "r")
        self.Data = json.loads(file.read())
        file.close()

class ContentReader(object): #文本解析中心
    pass

# json.dumps(a,sort_keys=True, indent=4, separators=(',', ': '))

def input(User, Content, IOList): #流水线，注意由于没有IOCallback，返回的必须是键值
    User = UserReader(User)
    if User.Read: #用户鉴权
        pass

    else: #非法用户区域
        try: #未注册用户输入的是数字？
            key = int(Content)
            if key == 0: #无key注册模式
                return User.register()

            else: #key注册模式，内部鉴权
                return User.register(key)

        except: #输入的不是数字
            return "Content.illegal"


