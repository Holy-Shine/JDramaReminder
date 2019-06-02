import urllib
import urllib.request as ur
import datetime
import pickle as pkl
import time
import os
import traceback
from tabulate import tabulate
from bs4 import BeautifulSoup

def checkData(url):
    req=ur.Request(url)
    res=ur.urlopen(req)
    bsObj = BeautifulSoup(res.read(),'html.parser')

    # 日剧信息块
    dataBlock=bsObj.find('div',class_='resource-tit')
    des=dataBlock.find('p').text

    # 获取剧名和更新信息
    (year, month, day)=datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day
    time=(year,month,day)
    state=des.split('/')[1]
    #print("{}-{}-{}".format(year, month, day))
    return state , time


'''
e.g.
bangumi_data={
    '东京单身男子':{'state':'更新至05回','year':2019,'month':6,'day':1, 'url':'http://www.zmz2019.com/resource/37927'}
}
'''
if __name__=='__main__':
    try:
        current_path = os.path.dirname(__file__)
        pklpath = current_path+os.path.sep+'bangumiData.p'

        bangumi_data=pkl.load(open(pklpath,'rb'))
        table=[]
        headers=['剧名','状态','更新时间','new']
        for key in bangumi_data.keys():
            bangumi=bangumi_data[key]

            # 剧的信息
            name=key
            url=bangumi['url']
            year, month, day=bangumi['year'],bangumi['month'],bangumi['day']
            old_state=bangumi['state']

            state , time=checkData(url)
            new=' '
            # 确认更新
            if(old_state!=state):
                # 更新表
                old_state = state
                year, month, day=time
                new='new!'

                # 更新dict信息
                bangumi['year']=year
                bangumi['month']=month
                bangumi['day']=day
                bangumi['state']=old_state

            table_item=[key, old_state, '{}-{}-{}'.format(year,month,day), new]
            table.append(table_item)

        pkl.dump(bangumi_data,open(pklpath,'wb'))
        print(tabulate(table, headers=headers, tablefmt='grid'))
    except Exception:
        print(Exception.message)