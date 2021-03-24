import difflib                                 #导入difflib模块
from difflib import SequenceMatcher



import difflib                                             #导入difflib模块
from difflib import get_close_matches                      #导入get_close_matches            
get_close_matches("rainn", ["help", "pyramid", "rain"])    #对比会自动输出rain


data.keys()                  #获取数据文档中的关键字——key值

get_close_matches("rainn", data.keys(), n=5)           #从数据库的关键字中选择n个（此处5个）和输入值rainn相近的关键字，key值
                                                       #也可以将n去除掉，会自动出现最匹配的几个相关键值

get_close_matches("rainn", data.keys(), cutoff=0.8)    #类似于加了一个筛选比率，比例高，相似高，显示数量少； 比率低，相似度低，显示数量多