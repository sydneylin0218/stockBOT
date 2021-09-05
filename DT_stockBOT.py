#!/usr/bin/env python
# -*- coding:utf-8 -*-

import discord
import json


with open("account.info", encoding="utf-8") as f:
    accountDICT = json.loads(f.read())
    
from ArticutAPI import Articut
articut = Articut(username= accountDICT["username"], apikey= accountDICT["apikey"])

from stockBOT import runLoki

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
                inputLIST = ["聯發科的基本資料"]
                filterLIST = []
                resultDICT = runLoki(inputLIST, filterLIST)
                print("Result => {}".format(resultDICT))
                
                print(resultDICT)
                
                if resultDICT["function"] == "information":
                    result_infoDICT = information(resultDICT["symbol"])
                    resultDICT.update(result_infoDICT)
                elif resultDICT["function"] == "growth":
                    result_growthDICT = growth(resultDICT["symbol"])
                    resultDICT.update(result_growthDICT)
                    
            
                if resultDICT["function"] == "information":
                    print(companyDICT[resultDICT["symbol"]][0]+resultDICT["symbol"]+"的公司基本資料如下！"+"\n公司名稱："+resultDICT["name"]+"\n產業別："+resultDICT["industry"]+"\n市值"+resultDICT["value"]+"\n主要業務："+resultDICT["business"])  
                elif resultDICT["function"] == "information":
                    print(companyDICT[resultDICT["symbol"]][0]+resultDICT["symbol"]+"的公司基本資料如下！"+"\n公司名稱："+resultDICT["name"]+"\n產業別："+resultDICT["industry"]+"\n市值"+resultDICT["value"]+"\n主要業務："+resultDICT["business"])    
                elif resultDICT["symbol"] == None:
                    print("不確定您要找哪一支股票的資訊！請再輸入一次股票名稱或是代號！")
                elif resultDICT["function"] == None:
                    print("不確定您要找哪一類的資訊！請再輸入一次要查的資料類別！")
                                    

if __name__ == "__main__":
    client = BotClient()
    client.run(accountDICT["discord_token"])