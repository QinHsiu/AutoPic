import matplotlib
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
        if self.frame_params["save_type"]=="pdf":
            matplotlib.use('PDF')
        plt.rcParams['font.family'] = [self.chart_params["font_family"]]  
        plt.rcParams['figure.figsize'] = eval(self.frame_params["fig_size"])
        plt.rcParams['font.size'] = self.chart_params["font_size"]
        plt.rcParams['ps.useafm'] = self.chart_params["useafm"]
        # plt.rcParams['pdf.use14corefonts'] = True
        # plt.rcParams['text.usetex'] = True
        # x_dot=range(len(self.data))
        for idx,(key,value) in enumerate(self.data.items()):
            # print(idx,key,value)
            plt.plot(range(len(value)),value,c=self.chart_params["colors"][idx],marker=self.chart_params["marks"][idx],label=key)
        
        plt.xticks(range(len(value)),self.chart_params["x_ticks"])        
        # plt.yticks(self.chart_params["y_ticks"])
        
        plt.ylabel(self.chart_params["y_label"])
        plt.xlabel(self.chart_params["x_label"])

        
        plt.legend(loc=eval(self.frame_params["loc"]))
        plt.savefig("./temp_pic/{0}.{1}".format(self.frame_params["save_name"],self.frame_params["save_type"]),dpi=600)


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