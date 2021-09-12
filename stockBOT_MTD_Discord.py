logging.basicConfig(level=logging.CRITICAL)

# <���o�h����ܸ�T>
client = discord.Client()
mscDICT = {# "userID": {Template}
           }

TemplateDICT = {"symbol": "","function": "", "updatetime":""}

# </���o�h����ܸ�T>

punctuationPat = re.compile("[,\.\?:;�A�C�H�B�G�F\n]+")

def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;�A�C�H�B�G�F\n]+")
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

    if not re.search("<@[!&]{}> ?".format(client.user.id), message.content):    # �u�� @Bot �~�|�^��
        return

    if message.author == client.user:
        return
    try:
        print("client.user.id =", client.user.id, "\nmessage.content =", message.content)
        msgSTR = re.sub("<@[!&]{}> ?".format(client.user.id), "", message.content)    # ���� User ���T���A�N id ���N�� ""
        print("msgSTR =", msgSTR)
        replySTR = ""    # Bot �^���T��

        if re.search("(hi|hello|���o|��|[�A�z]�n)", msgSTR.lower()):
            replySTR = "Hi �z�n�A�аݷQ�d�߭����Ѳ���ƩO�H"
            await message.reply(replySTR)
            return    
        
        lokiResultDICT = getLokiResult(msgSTR)    # ���o Loki �^�ǵ��G
        
        if lokiResultDICT:
            if client.user.id not in mscDICT:    # �P�_ User �O�_���Ĥ@�����
                mscDICT[client.user.id] = {"symbol": "",
                                           "function": "",
                                           "updatetime":"",
                                           "completed": False}     
                
                
    except Exception as e:
        logging.error("[MSG ERROR] {}".format(str(e)))
        print("[MSG ERROR] {}".format(str(e)))