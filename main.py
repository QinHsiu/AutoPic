import gradio as gr
import numpy as np
import random

from utils import *
from pics import *
from PIL import Image    


#需要的参数有：原始数据（以字典形式）、图的类型（折现、散点、柱状）、图线的特征（颜色、标记、标记大小，线条宽度）、图框的特征（标签是否加框、是否加格子，每个图标签的位置）
def data2pic(data_file,chart_type,chart_params,frame_params):
    # Save the uploaded file to the specified path
    path="./temp_data/"
    os.makedirs(path, exist_ok=True)
    data_file.save(os.path.join(path, data_file.name))
    
    data=data_process(os.path.join(path, data_file.name))
    
    if chart_type=="linear":
        res_chart=LinearChart(data,chart_params,frame_params)
    elif chart_type=="scatter":
        res_chart=ScatterChart(data,chart_params,frame_params)
    elif res_chart=="bar":
        res_chart=BarChart(data,chart_params,frame_params)
    else:
        raise ValueError("The type of the chart is not exist. Make sure chart type in [linear,scatter,bar]")
    
    res_chart.save_pic()
    img=Image.open("./temp_pic/data."+frame_params["save_type"])
    img_data=img.convert("RGB").tobytes()
    return img_data
    
        
# 获取数据，数据存放格式：每一行两个元素，前面是一串数字，后面是他的标签，两者用空格分开
data_file=gr.inputs.File(label="Upload data file")

# 获取参数
chart_types=["linear","bar","scatter"]
chart_params={"color":[],"mark":[],"mark_size":[],"line_width":[]}
frame_params={"is_frame":0,"is_grid":0,"loc":(0,0),"save_type":"png"}

chart_type=gr.inputs.Dropdown(chart_types,default="linear",label="chart type")

chart_params["color"] = gr.inputs.Textbox(default="", label="color")
chart_params["mark_size"] = gr.inputs.Slider(0.1, 2, step=0.1, default=1.0, label="mark size")
chart_params["line_width"]= gr.inputs.Slider(0.1, 2, step=0.1, default=1.0, label="line width")

frame_params["is_frame"]=gr.Dropdown([0,1],default=0,label="use frame")
frame_params["is_grid"]=gr.Dropdown([0,1],default=0,label="use grid")
frame_params["loc"]= gr.inputs.Textbox(default="(0,0)", label="loc")
frame_params["save_type"]=gr.Dropdown(["png","pdf","jpg"],default="png",label="save type")


# 创建交互式界面
iface = gr.Interface(fn=data2pic, inputs=[data_file,chart_type,chart_params,frame_params], outputs=gr.outputs.Image(), 
                     title='Data to Chart Web App', description='Convert datas to chart')


# 启动网站
if __name__ == '__main__':
    iface.launch(server_name='0.0.0.0', server_port=8802, show_error=True, debug=True, share=True, inbrowser=True)
