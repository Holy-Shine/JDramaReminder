import argparse
import os
import pickle as pkl
'''
headers=['剧名','状态','更新时间','new']

e.g.

'东京单身男子':{'state':'更新至05回','year':2019,'month':6,'day':1, 'url':'http://www.zmz2019.com/resource/37927'}
'''

def getArgs():

    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=True,type=str,help='bangumi name')
    parser.add_argument('--url',type=str, help='bangumi url',default=None)
    parser.add_argument('--delete',type=bool,default=False)
    '''
    name=parser.name
    url=parser.url
    
    userparams={
        'name':name,
        'url':url
    }
    return userparams
    '''
    return parser.parse_args()
 
if __name__=='__main__':
    args=getArgs()
    name, url, delete=args.name, args.url, args.delete
    if delete==False and url==None:
        print('没有指定番剧的url!')
        exit(0)
    current_path = os.path.dirname(__file__)
    pklpath = current_path+os.path.sep+'bangumiData.p'
    
    bangumi_data=pkl.load(open(pklpath,'rb'))
    
        
    if delete:
        if name not in bangumi_data.keys():
            print('现有列表里没有指定的番剧！')
            exit(0)
        bangumi_data.pop(name)
    else:
        bangumi_data[name]={}
        bangumi_data[name]['url']=url
        bangumi_data[name]['year']=None
        bangumi_data[name]['month']=None
        bangumi_data[name]['day']=None
        bangumi_data[name]['state']=None
    pkl.dump(bangumi_data,open(pklpath,'wb'))
        