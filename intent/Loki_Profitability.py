#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Profitability

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Profitability = True
userDefinedDICT = {"2302": ["麗正", "2302"], "2303": ["聯電", "2303"], "2329": ["華泰", "2329"], "2330": ["台積電", "2330"], "2337": ["旺宏", "2337"], "2338": ["光罩", "2338"], "2342": ["茂矽", "2342"], "2344": ["華邦電", "2344"], "2351": ["順德", "2351"], "2363": ["矽統", "2363"], "2369": ["菱生", "2369"], "2379": ["瑞昱", "2379"], "2388": ["威盛", "2388"], "2401": ["凌陽", "2401"], "2408": ["南亞科", "2408"], "2434": ["統懋", "2434"], "2436": ["偉詮電", "2436"], "2441": ["超豐", "2441"], "2449": ["京元電子", "京元", "2449"], "2451": ["創見", "2451"], "2454": ["聯發科", "2454"], "2458": ["義隆", "2458"], "3006": ["晶豪科", "3006"], "3014": ["聯陽", "3014"], "3016": ["家晶", "3016"], "3034": ["聯詠", "3034"], "3041": ["揚智", "3041"], "3054": ["立萬利", "3054"], "3094": ["聯傑", "3094"], "3189": ["景碩", "3189"], "3257": ["虹冠電", "3257"], "3413": ["京鼎", "3413"], "3443": ["創意", "3443"], "3450": ["聯鈞", "3450"], "3530": ["晶相光", "3530"], "3532": ["台勝科", "3532"], "3536": ["誠創", "3536"], "3545": ["敦泰", "3545"], "3583": ["辛耕", "3583"], "3588": ["通嘉", "3588"], "3661": ["世芯-KY", "3661"], "3686": ["達能", "3686"], "3711": ["日月光投控", "3711"], "4919": ["新唐", "4919"], "4952": ["凌通", "4952"], "4961": ["天銓", "4961"], "4967": ["十銓", "4967"], "4968": ["立積", "4968"], "5269": ["祥碩", "5269"], "5285": ["界霖", "5285"], "5471": ["松翰", "5471"], "6202": ["盛群", "6202"], "6239": ["力成", "6239"], "6243": ["迅杰", "6243"], "6257": ["矽格", "6257"], "6271": ["同欣電", "6271"], "6415": ["矽力-KY", "矽力", "6415"], "6451": ["訊芯-KY", "訊芯", "6451"], "6515": ["穎崴", "6515"], "6525": ["捷敏-KY", "捷敏", "6525"], "6531": ["愛普", "6531"], "6533": ["晶心科", "6533"], "6552": ["易華電", "6552"], "6573": ["虹揚-KY", "6573"], "6756": ["威鋒電子", "6756"], "8016": ["矽創", "8016"], "8028": ["昇陽半導體電子", "8028"], "8081": ["致心", "8081"], "8110": ["華東", "8110"], "8131": ["福懋科", "8131"], "8150": ["南茂", "8150"], "8261": ["富鼎", "8261"], "8271": ["宇瞻", "8271"], "安全性": [""], "成交價": [""], "成長力": [""], "成長率": ["YOY", "yoy"], "流動比": ["流動比率"], "負債比": [""], "速動比": ["速動比率"], "基本資料": ["資料", "資訊", "基本資料", "基本資訊"], "年成長率": [""], "每股盈餘": [""], "營業利益": [""], "營業收入": ["營收", "營業收入"], "稅後淨利": [""], "財務報表": ["財務報表", "財報", "財報資料", "基本財報資料"], "存貨周轉率": [""], "安全性分析": [""], "安全性指標": [""], "昨日收盤價": ["昨收", "昨日收盤價"], "流速動比率": [""], "現金流量比": [""], "利息保障倍數": [""], "營運周轉能力": [""], "資產年成長率": [""], "應收帳款週轉率": [""], "每股盈餘成長率": [""], "股東權益報酬率": [""]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Profitability:
        print("[Profitability] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[聯發科]ROA及ROE":
        resultDICT["fun_profitability"] = True

    if utterance == "[聯發科]ROEROA":
        resultDICT["fun_profitability"] = True

    if utterance == "[聯發科]ROE及ROA":
        resultDICT["fun_profitability"] = True
        
    if utterance == "[聯發科]利潤比率":
        resultDICT["fun_profitability"] = True

    if utterance == "[聯發科]存貨周轉率":
        resultDICT["fun_profitability"] = True
        
    if utterance == "[聯發科]營運周轉能力":
       resultDICT["fun_profitability"] = True

    if utterance == "[聯發科]獲利[相關]指標":
        resultDICT["fun_profitability"] = True

    if utterance == "[聯發科]獲利情形":
        resultDICT["fun_profitability"] = True
    
    if utterance == "[聯發科]獲利情況":
        resultDICT["fun_profitability"] = True

    if utterance == "[聯發科]獲利指標":
        resultDICT["fun_profitability"] = True

    if utterance == "[聯發科]獲利能力":
        resultDICT["fun_profitability"] = True

    if utterance == "[聯發科]的ROA":
        resultDICT["fun_profitability"] = True
        
    if utterance == "[聯發科]的ROE":
        resultDICT["fun_profitability"] = True

    if utterance == "[聯發科]股東權益報酬率":
        resultDICT["fun_profitability"] = True

    if utterance == "[聯發科]資產報酬率":
        resultDICT["fun_profitability"] = True

    if utterance == "[連發科]應收帳款週轉率":
        resultDICT["fun_profitability"] = True
        
    return resultDICT