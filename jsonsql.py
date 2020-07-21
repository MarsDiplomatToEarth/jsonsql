# coding=utf-8
import json,os,sys,codecs,chardet

version = 2
if sys.version_info >= (3,3):
    version = 3
print("now python version:"+str(version))

if version == 2:
    pass
else:
    pass
   
#json file and dictionary engine
def connectjsondsql(namen="unname"):
    #if json file exists:
    if os.path.exists(namen+'.json') and os.path.getsize(namen+'.json'): 
        print("exist,now connectting")
    elif os.path.exists(namen+'.json') and not os.path.getsize(namen+'.json'):
        print("exist,but null")
        if version == 2:
            with codecs.open(namen+'.json','w+',encoding='utf-8')as fp:
                json.dump({},fp,ensure_ascii=False)
        else:
            with open(namen+'.json','w+',encoding='utf8')as fp:
                json.dump({},fp,ensure_ascii=False)
    else:
        print("not exist,now creating and connectting")
        if version == 2:
            with codecs.open(namen+'.json','a+',encoding='utf-8')as fp:
                json.dump({},fp,ensure_ascii=False)
        else:
            with open(namen+'.json','a+',encoding='utf8')as fp:
                json.dump({},fp,ensure_ascii=False)
    return namen+'.json'
    
    
def cjds(namen="unname"):
    return connectjsondsql(namen)
    
def printjd(name):
    if version == 2:
        with codecs.open(name,'r+',encoding='utf-8')as fp:
            json_data = json.load(fp)
    else:
        with open(name,'r+',encoding='utf8')as fp:
            json_data = json.load(fp)
    print('printf data: ',json_data)
    print('printf data type: ', type(json_data))
    if not isinstance(json_data,dict):
        return {}
    else:
        return json_data

def returnjd(name):
    if version == 2:
        with codecs.open(name,'r+',encoding='utf-8')as fp:
            json_data = json.load(fp)
    else:
        with open(name,'r+',encoding='utf8')as fp:
            json_data = json.load(fp)
    if not isinstance(json_data, dict):
        return {}
    else:
        return json_data
        
def renewjd(name,dic):
    if version == 2:
        with codecs.open(name,'w+',encoding='utf-8')as fp:
            json.dump(dic,fp,ensure_ascii=False)
    else:
        with open(name,'w+',encoding='utf8')as fp:
            json.dump(dic,fp,ensure_ascii=False)
    return True

#dictionary function 
#key to value https://www.runoob.com/python/python-dictionary.html
#value to key https://blog.csdn.net/ywx1832990/article/details/79145576

#list function
#list https://www.runoob.com/python/python-lists.html
    
local = cjds(namen = "1")
x = printjd(local)
x['d'] = 123

print( returnjd(local))
renewjd( local,x )
print( returnjd(local))
