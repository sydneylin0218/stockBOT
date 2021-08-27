
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
from requests import post
from requests import codes

def information(symbol):
    URL = "https://goodinfo.tw/StockInfo/StockDetail.asp?STOCK_ID="+ symbol 
    print(URL)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    r = requests.post(url=URL,headers=headers)
    html =BeautifulSoup(r.content, "html.parser")
    
    result_infoDICT = {}
    
    table = html.findAll("table")[40]
    table_row_name=table.findAll("tr")[1]
    td_name = table_row_name.findAll("td")[1]
    name = td_name.text
    result_infoDICT["name"] = name
    
    
    table_row_industry=table.findAll("tr")[2]
    td_industry=table_row_industry.findAll("td")[1]
    industry=td_industry.text
    result_infoDICT["industry"] = industry
    

    table_row_value=table.findAll("tr")[4]
    td_value = table_row_value.findAll("td")[3]
    value = td_value.text
    result_infoDICT["value"] = value    


    table_row_business=table.findAll("tr")[14]
    td_business = table_row_business.findAll("td")[0]
    business = td_business.text
    result_infoDICT["business"] = business    
    
    return result_infoDICT
    