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