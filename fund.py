import requests
import threading
import os
from config import *

if os.path.exists('Fund.txt') :os.remove('Fund.txt')
total_today_income = 0
total_income = 0

def display_info(code):
    #url = 'http://hq.sinajs.cn/list=' + code +''
    url='http://fundgz.1234567.com.cn/js/' + code +'.js?rt=1463558676006'
    response = requests.get(url).text
    return response

def out_put(doc):
    global total_today_income
    global total_income
    f = open('fund.txt','a')
    out_docs = [doc['name'][:11],':','\t',doc['money'],'元','\t','当前收益为：',' ',doc['income_today'],'\t','总收益为：',doc['income_totally'],
                '(',doc['total_growth_rate'],')','\t','增长率：',doc['growth rate'],'\t','当前净值：',doc['net value'],'(',doc['reference_rate'],
                ')','\t',doc['time'],'\n'] 
    for out_doc in out_docs:
        f.write(out_doc)
    total_today_income = total_today_income + float(doc['income_today'])
    total_income = total_income +float(doc['income_totally'])
    incomes = ['总收益：',str(total_income)[:6],'\t','今日收益：',str(total_today_income)[:6]]
    f.close()
    return incomes

def deal_info(response,initial_value,share,suggest_value):
    response = response.split('"')
    if len(response[7])<8:
        response[7] = response[7] +'\t'
    doc = {
        'name': response[7],
        'time': response[27],
        'net value': response[19],
        'growth rate': response[23],
        'initial value': initial_value,
        'share': share,
        'income_today': str(float(share)*(float(response[19])-float(response[15])))[:5],
        'income_totally': str(round(float(share)*(float(response[19])-float(initial_value)))),
        'money': str(round(float(initial_value)*float(share))),
        'reference_rate':str((float(response[19])/float(suggest_value)-1)*100)[:5],
        'total_growth_rate': str((float(response[19])/float(initial_value)-1)*100)[:5]
        }
    return doc

def total_earnings(doc):
    total_today_income = 0
    total_income = 0
    
    

def main():

    for code in codes:
        response = display_info(code[0])
        doc = deal_info(response, code[1],code[2],code[3])
        incomes = out_put(doc)
    f = open('fund.txt','a')
    for income in incomes:
        f.write(income)
    f.close()

if __name__=='__main__':
    main()