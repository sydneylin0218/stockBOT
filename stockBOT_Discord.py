#!/usr/bin/env python
# -*- coding:utf-8 -*-

import discord
import json
import logging
import re
from fc_info import information
from fc_info import growth
from DICT import companyDICT

with open("account.info", encoding="utf-8") as f:
    accountDICT = json.loads(f.read())
    
from ArticutAPI import Articut
articut = Articut(username= accountDICT["username"], apikey= accountDICT["apikey"])

from stockBOT_Loki import runLoki

logging.basicConfig(level=logging.CRITICAL)

# <取得多輪對話資訊>
client = discord.Client()
mscDICT = {# "userID": {Template}
           }

TemplateDICT = {"symbol": "","function": "", "updatetime":""}

# </取得多輪對話資訊>

punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")

def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Loki Result => {}".format(resultDICT))
    return resultDICT

@client.event
async def on_ready():
    logging.info("[READY INFO] {} has connected to Discord!".format(client.user))
    print("[READY INFO] {} has connected to Discord!".format(client.user))


@client.event
async def on_message(message):
    if message.channel.name != "bot_test":
        return

    if not re.search("<@[!&]{}> ?".format(client.user.id), message.content):    # 只有 @Bot 才會回應
        return

    if message.author == client.user:
        return
    try:
        print("client.user.id =", client.user.id, "\nmessage.content =", message.content)
        msgSTR = re.sub("<@[!&]{}> ?".format(client.user.id), "", message.content)    # 收到 User 的訊息，將 id 取代成 ""
        print("msgSTR =", msgSTR)
        replySTR = ""    # Bot 回應訊息

        if re.search("(hi|hello|哈囉|嗨|[你您]好)", msgSTR.lower()):
            replySTR = "Hi 您好，請問想查詢哪類股票資料呢？"
            await message.reply(replySTR)
            return    
        
        lokiResultDICT = getLokiResult(msgSTR)    # 取得 Loki 回傳結果
        
        if lokiResultDICT:
            if client.user.id not in mscDICT:    # 判斷 User 是否為第一輪對話
                mscDICT[client.user.id] = {"symbol": "",
                                           "function": "",
                                           "updatetime":"",
                                           "completed": False}     
                
                
    except Exception as e:
        logging.error("[MSG ERROR] {}".format(str(e)))
        print("[MSG ERROR] {}".format(str(e)))
        


class BotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {} with id {}'.format(self.user, self.user.id))

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author == self.user:
            return None

        print("到到來自 {} 的訊息".format(message.author))
        print("訊息內容是 {}。".format(message.content))
        if self.user.mentioned_in(message):
            print("本 bot 被叫到了！")
            msg = message.content.replace("<@!{}> ".format(self.user.id), "")
            if msg == 'ping':
                await message.reply('pong')
            if msg == 'ping ping':
                await message.reply('pong pong')
            else:
                inputLIST = [msg]
                filterLIST = []
                resultDICT = runLoki(inputLIST, filterLIST)
                print("Result => {}".format(resultDICT))
                
                print(resultDICT)
                
                if  resultDICT["fun_information"] == True:
                    result_infoDICT = information(resultDICT["symbol"])
                    resultDICT.update(result_infoDICT)
                elif resultDICT["fun_growth"] == True:
                    result_growthDICT = growth(resultDICT["symbol"])
                    resultDICT.update(result_growthDICT)
                    
            
                if resultDICT["fun_information"] == True:
                    await message.reply(companyDICT[resultDICT["symbol"]][0]+resultDICT["symbol"]+"的公司基本資料如下！"+"\n公司名稱："+resultDICT["name"]+"\n產業別："+resultDICT["industry"]+"\n市值："+resultDICT["value"]+"\n主要業務："+resultDICT["business"])  
                elif resultDICT["fun_growth"] == True:
                    await message.reply(companyDICT[resultDICT["symbol"]][0]+resultDICT["symbol"]+"的獲利年成長率如下！"+"\n營收年成長率："+resultDICT["revenue_YOY"]+"\n毛利年成長率："+resultDICT["gross_profit_YOY"]+"\n營業利益年成長率："+resultDICT["operating_income_YOY"]+"\n稅前淨利年成長率："+resultDICT["NIBT_YOY"]+"\n稅後淨利年成長率："+resultDICT["NI_YOY"]+"\n每股稅後盈餘年成長率："+resultDICT["EPS_YOY"])    
                elif resultDICT["symbol"] == None:
                    await message.reply("不確定您要找哪一支股票的資訊！請再輸入一次股票名稱或是代號！")
                else:
                    await message.reply("不確定您要找哪一類的資訊！請再輸入一次要查的資料類別！")
                                    

if __name__ == "__main__":
    client = BotClient()
    client.run(accountDICT["discord_token"])