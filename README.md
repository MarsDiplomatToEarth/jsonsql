# jsonsql
Python function about json. 

还有一些问题，比如python2情况下会报错,错误如下，请问发生了什么

Traceback (most recent call last):
  File "D:\code\python\func\jsonsql.py", line 79, in <module>
    x = printj(server)
  File "D:\code\python\func\jsonsql.py", line 40, in printj
    json_data = json.load(fp)
  File "D:\anaconda\envs\py2\lib\json\__init__.py", line 291, in load
    **kw)
  File "D:\anaconda\envs\py2\lib\json\__init__.py", line 339, in loads
    return _default_decoder.decode(s)
  File "D:\anaconda\envs\py2\lib\json\decoder.py", line 364, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "D:\anaconda\envs\py2\lib\json\decoder.py", line 382, in raw_decode
    raise ValueError("No JSON object could be decoded")
ValueError: No JSON object could be decoded
