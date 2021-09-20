#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Safety

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Safety = True
userDefinedDICT = {"2302": ["2302", "麗正"], "2303": ["2303", "聯電"], "2329": ["2329", "華泰"], "2330": ["2330", "台積電"], "2337": ["2337", "旺宏"], "2338": ["2338", "光罩"], "2342": ["2342", "茂矽"], "2344": ["2344", "華邦電"], "2351": ["2351", "順德"], "2363": ["2363", "矽統"], "2369": ["2369", "菱生"], "2379": ["2379", "瑞昱"], "2388": ["2388", "威盛"], "2401": ["2401", "凌陽"], "2408": ["2408", "南亞科"], "2434": ["2434", "統懋"], "2436": ["2436", "偉詮電"], "2441": ["2441", "超豐"], "2449": ["2449", "京元", "京元電子"], "2451": ["2451", "創見"], "2454": ["2454", "聯發科"], "2458": ["2458", "義隆"], "3006": ["3006", "晶豪科"], "3014": ["3014", "聯陽"], "3016": ["3016", "家晶"], "3034": ["3034", "聯詠"], "3041": ["3041", "揚智"], "3054": ["3054", "立萬利"], "3094": ["3094", "聯傑"], "3189": ["3189", "景碩"], "3257": ["3257", "虹冠電"], "3413": ["3413", "京鼎"], "3443": ["3443", "創意"], "3450": ["3450", "聯鈞"], "3530": ["3530", "晶相光"], "3532": ["3532", "台勝科"], "3536": ["3536", "誠創"], "3545": ["3545", "敦泰"], "3583": ["3583", "辛耕"], "3588": ["3588", "通嘉"], "3661": ["3661", "世芯-KY"], "3686": ["3686", "達能"], "3711": ["3711", "日月光投控"], "4919": ["4919", "新唐"], "4952": ["4952", "凌通"], "4961": ["4961", "天銓"], "4967": ["4967", "十銓"], "4968": ["4968", "立積"], "5269": ["5269", "祥碩"], "5285": ["5285", "界霖"], "5471": ["5471", "松翰"], "6202": ["6202", "盛群"], "6239": ["6239", "力成"], "6243": ["6243", "迅杰"], "6257": ["6257", "矽格"], "6271": ["6271", "同欣電"], "6415": ["6415", "矽力", "矽力-KY"], "6451": ["6451", "訊芯", "訊芯-KY"], "6515": ["6515", "穎崴"], "6525": ["6525", "捷敏", "捷敏-KY"], "6531": ["6531", "愛普"], "6533": ["6533", "晶心科"], "6552": ["6552", "易華電"], "6573": ["6573", "虹揚-KY"], "6756": ["6756", "威鋒電子"], "8016": ["8016", "矽創"], "8028": ["8028", "昇陽半導體電子"], "8081": ["8081", "致心"], "8110": ["8110", "華東"], "8131": ["8131", "福懋科"], "8150": ["8150", "南茂"], "8261": ["8261", "富鼎"], "8271": ["8271", "宇瞻"], "安全性": [""], "成交價": [""], "成長力": [""], "成長率": ["YOY", "yoy"], "流動比": ["流動比率"], "負債比": [""], "速動比": ["速動比率"], "基本資料": ["基本資料", "基本資訊", "資料", "資訊"], "年成長率": [""], "每股盈餘": [""], "營業利益": [""], "營業收入": ["營收", "營業收入"], "稅後淨利": [""], "財務報表": ["基本財報資料", "財務報表", "財報", "財報資料"], "運輸類股": ["2601", "益航", "2603", "長榮", "2604", "立榮", "2605", "新興", "2606", "裕民", "2607", "榮運", "2608", "大榮", "2609", "陽明", "2610", "華航", "2611", "志信", "2612", "中航", "2613", "中櫃", "2614", "遠森科", "2615", "萬海", "2616", "山隆", "2617", "台航", "2618", "長榮航"], "存貨周轉率": [""], "安全性分析": [""], "安全性指標": [""], "昨日收盤價": ["昨收", "昨日收盤價"], "流速動比率": [""], "現金流量比": [""], "利息保障倍數": [""], "營運周轉能力": [""], "資產年成長率": [""], "應收帳款週轉率": [""], "每股盈餘成長率": [""], "股東權益報酬率": [""]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Safety:
        print("[Safety] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    
    if utterance == "[聯發科][安全]嗎":
        resultDICT["fun_safety"] = True


    if utterance == "[聯發科]償債能力":
        resultDICT["fun_safety"] = True


    if utterance == "[聯發科]利息保障倍數":
        resultDICT["fun_safety"] = True


    if utterance == "[聯發科]安全性":
        resultDICT["fun_safety"] = True


    if utterance == "[聯發科]安全性分析":
        resultDICT["function"] = "safty"

    if utterance == "[聯發科]安全性指標":
        resultDICT["fun_safety"] = True


    if utterance == "[聯發科]是不[是][安全]的股票":
        resultDICT["fun_safety"] = True


    if utterance == "[聯發科]流動比":
        resultDICT["fun_safety"] = True


    if utterance == "[聯發科]流速動比率":
        resultDICT["fun_safety"] = True


    if utterance == "[聯發科]現金流量比":
        resultDICT["fun_safety"] = True


    if utterance == "[聯發科]負債":
        resultDICT["fun_safety"] = True


    if utterance == "[聯發科]負債比":
        resultDICT["fun_safety"] = True


    if utterance == "[聯發科]速動比":
        resultDICT["fun_safety"] = True


    return resultDICT