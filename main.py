import gradio as gr
import numpy as np
import random
import matplotlib.font_manager as fm
import tempfile

from utils import *
from pics import *
from PIL import Image
from flask import Flask,request
import json    


#需要的参数有：原始数据（以字典形式）、图的类型（折现、散点、柱状）、图线的特征（颜色、标记、标记大小，线条宽度）、图框的特征（标签是否加框、是否加格子，每个图标签的位置）
def data2pic(font_family,chart_type,save_name): 
    print(data)
    print(config)
       
    chart_params['font_family']=font_family
    frame_params["save_name"]=save_name
    if chart_type=="linear":
        res_chart=LinearChart(data,chart_params,frame_params)
    elif chart_type=="scatter":
        res_chart=ScatterChart(data,chart_params,frame_params)
    elif res_chart=="bar":
        res_chart=BarChart(data,chart_params,frame_params)
    else:
        raise ValueError("The type of the chart is not exist. Make sure chart type in [linear,scatter,bar]")
    
    res_chart.save_pic()
    img=Image.open("./temp_pic/{0}.{1}".format(save_name,frame_params["save_type"]))
    # img_data=img.convert("RGB").tobytes()
    return img
    
        
# 获取数据，数据存放格式：每一行两个元素，前面是一串数字，后面是他的标签，两者用空格分开
data=data_process("./temp_data/data.txt")

# 获取配置文件，配置文件以字典格式进行存放
with open("./temp_config/config.json","r+") as fr:
    config=json.load(fr)
chart_params=config["chart_params"]
frame_params=config["frame_params"]


# 获取字体类型
font_familes=fm.findSystemFonts()
font_family=gr.inputs.Dropdown(font_familes,default="Times New Roma",label="font family")

# 获取参数
# chart_params={"colors":[],"marks":[],"mark_size":[],"line_width":[],"x_label":"","y_label":"","x_ticks":[],"y_ticks":[],"x_lim":[],"y_lim":[],"font_size":[]}
# frame_params={"is_frame":0,"is_grid":0,"loc":(0,0),"save_type":"png","fig_size":"(10,6)"}


# 获取图片保存类型
chart_types=["linear","bar","scatter"]
chart_type=gr.inputs.Dropdown(chart_types,default="linear",label="chart type")

save_name=gr.inputs.Textbox(default="", label="save name")



# chart_params["x_label"]=gr.inputs.Textbox(default="", label="x label")
# chart_params["y_label"]=gr.inputs.Textbox(default="", label="y label")
# chart_params["x_ticks"]=gr.inputs.Textbox(default="", label="x ticks")
# chart_params["y_ticks"]=gr.inputs.Textbox(default="", label="y ticks")
# chart_params["x_lim"]=gr.inputs.Textbox(default="", label="x lim")
# chart_params["y_lim"]=gr.inputs.Textbox(default="", label="y lim")
# chart_params["colors"] = gr.inputs.Textbox(default="", label="colors")
# chart_params["marks"] = gr.inputs.Textbox(default="", label="marks")
# chart_params["mark_size"] = gr.inputs.Slider(0.1, 2, step=0.1, default=1.0, label="mark size")
# chart_params["line_width"]= gr.inputs.Slider(0.1, 2, step=0.1, default=1.0, label="line width")
# chart_params["font_size"]= gr.inputs.Slider(1, 100, step=1, default=20, label="font size")
# chart_params["font_family"]=gr.Dropdown(font_familes,default="Times New Roma",label="font family")

# 仅仅支持windowns  
# chart_params["useafm"]= gr.inputs.Slider(0, 1, step=1, default=1, label="useafm")
# frame_params["save_name"]=gr.inputs.Textbox(default="", label="save name")
# frame_params["fig_size"]=gr.inputs.Textbox(default="(10,6)", label="figure size")
# frame_params["is_frame"]=gr.Dropdown([0,1],default=0,label="use frame")
# frame_params["is_grid"]=gr.Dropdown([0,1],default=0,label="use grid")
# frame_params["loc"]= gr.inputs.Textbox(default="(0,0)", label="loc")
# frame_params["save_type"]=gr.Dropdown(["png","pdf","jpg"],default="png",label="save type")


# 获取配置文件
# config_file=gr.inputs.File(label="Upload config file.")



# 创建交互式界面
iface = gr.Interface(fn=data2pic, inputs=[font_family,chart_type,save_name], outputs="image", 
                     title='Data to Chart Web App', description='Convert datas to chart')


# 启动网站
if __name__ == '__main__':
    iface.launch(server_name='0.0.0.0', server_port=8803, show_error=True, debug=True, share=True, inbrowser=True)
