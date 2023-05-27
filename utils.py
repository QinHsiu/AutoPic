# 存放所有数据处理函数
import os

# 简单数据处理函数，返回字典形式存放的数据
def data_process(path):
    with open(path,"r+") as fr:
        data=fr.readlines()
    res_dic={}
    for d in data:
        d=d.strip("\n")
        d=d.split(" ")
        print(d)
        # 去掉换行符号
        values,key=d[:-1],d[-1]
        res_dic[key]=list(map(float,values))
    return res_dic
        