import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
# import orangecontrib.associate.fpgrowth as oaf  #进行关联规则分析的包


# 表格数据包括每日菜品名称、价格、被点的次数、每个订单花费、每个订单人数、就餐时间段、
#
# 分析菜品之间的联系（比如说点了A菜的点B菜的概率）
#
# 分析每天的客流量，标注出节假日、周末等情况


class ProData(object):

    def __init__(self, uploadfile):
        # 返回dataframe数据
        self.data = pd.read_excel(uploadfile)

    def deal(self):
        plt.figure()

        plt.show()

    # 十份饼图，显示销量前9名菜名和其他占总卖出百分比
    def sales(self):
        plt.figure()

        plt.pie()
        plt.show()
        pass

    # 较贵菜品出现在几人桌比较频繁
    def expensive(self):
        pass

    # A菜和B菜之间的关系
    def connection(self):
        pass
