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

def connectjsonsql(name="unname"):
    #if json file exists:
    if os.path.exists(name+'.json'):
        print("exist,now connectting")
    else:
        print("not exist,now creating and connectting")
        if version == 2:
            with codecs.open(name+'.json','a',encoding='utf-8')as fp:
                json.dump("",fp,ensure_ascii=False)
        else:
            with open(name+'.json','a',encoding='utf8')as fp:
                json.dump("",fp,ensure_ascii=False)
    return name+'.json'
    
def cjs(name="unname"):
    return connectjsonsql(name)
    
def printj(name):
    if version == 2:
        with codecs.open(name,'r',encoding='utf-8-sig')as fp:
            if(not bool(fp.read())):
                print("empty------------------------------------------------")
                return ""
            json_data = json.load(fp)
    else:
        with open(name,'r',encoding='utf8')as fp:
            json_data = json.load(fp)
    print('printf data：',json_data)
    print('printf data type：', type(json_data))
    if isinstance(json_data, str):
        return {}
    else:
        return json_data

def returnj(name):
    if version == 2:
        with codecs.open(name,'r',encoding='utf8')as fp:
            if(not bool(fp.read())):
                print("empty------------------------------------------------")
                return ""
            json_data = json.load(fp)
    else:
        with open(name,'r',encoding='utf8')as fp:
            json_data = json.load(fp)
    if isinstance(json_data, str):
        return {}
    else:
        return json_data


def renewj(name,dic):
    if version == 2:
        with open(name,"w") as f:
            json.dump(dic,f,ensure_ascii=False)
    else:
        with open(name,"w",encoding='utf8') as f:
            json.dump(dic,f,ensure_ascii=False)
    print('printf data：',json_data)
    print('printf data type：', type(json_data))
    return json_data
    
server = cjs(name = "1")
x = printj(server)
