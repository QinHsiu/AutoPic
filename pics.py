import matplotlib.pyplot as plt


class BaseChart():
    def __init__(self,data,chart_params,frame_params) -> None:
        self.data=data
        self.chart_params=chart_params
        self.frame_params=frame_params
        self.save_path="./temp_pic/"
    def save_pic(self):
        # 绘制、保存图像
        raise NotImplementedError("Subclass must implement abstract method")

class LinearChart(BaseChart):
    def __init__(self,data,chart_params,frame_params) -> None:
        super().__init__(data,chart_params,frame_params)
    def save_pic(self):
        pass

class ScatterChart(BaseChart):
    def __init__(self,data,chart_params,frame_params) -> None:
        super().__init__(data,chart_params,frame_params)
    def save_pic(self):
        pass
    
    
class BarChart(BaseChart):
    def __init__(self,data,chart_params,frame_params) -> None:
        super().__init__(data,chart_params,frame_params)    
    def save_pic(self):
        pass    