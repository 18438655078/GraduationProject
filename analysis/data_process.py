# coding=utf-8
import pandas as pd
import numpy as np
import datetime
from matplotlib import pyplot as plt
import time
import os


# 绝对地址上一层
# windows路径
# address = os.path.dirname(__file__)
# address = address.split("\\")[:-1]
# address = r'/'.join(address)
# linux路径
address = os.path.dirname(__file__)
print(address)
address = address.split("/")[:-1]
address = r'/'.join(address)


class DataProcess(object):

    def __init__(self, dishes_info, order_info):
        self.dishes_info = dishes_info
        self.order_info = order_info
        self.img1 = None
        self.img2 = None
        self.img3 = None
        self.avgcount = None
        self.menavg = None
        self.dishe_avg = None
        self.use_time = None

    def deal(self):
        # dishes_info = pd.read_excel('dishes_info.xlsx')
        dishe_name = self.dishes_info['dishes_name']
        # 去除空白
        dishe_name = dishe_name.str.strip().values
        # print(type(dishe_name))
        # print(dishe_name)
        # 统计一共卖出多少菜品
        allnum = dishe_name.shape[0]
        # print(allnum)
        # 统计每个菜分别卖出了多少
        arr = dishe_name
        key = np.unique(arr)
        dishes_dict = {}
        for k in key:
            mask = (arr == k)
            arr_new = arr[mask]
            v = arr_new.size
            dishes_dict[k] = v
        dishes_tup = sorted(dishes_dict.items(), key=lambda x: x[1], reverse=True)

        plt.figure()
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签windows
        labels = []
        sizes = []
        for i in dishes_tup[:15]:
            labels.append(i[0])
            sizes.append(i[1])
        labels.append('其他')
        sizes.append(allnum)
        explode = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
        plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', shadow=False, startangle=150)
        num = 0
        for i in dishes_tup[:15]:
            labels.append(i[0])
            sizes.append(i[1])
            num += i[1]
        plt.title("饼图示例-销量前十五，共占总额%s%%" % str(num * 100 // int(allnum)))
        millis = str(int(round(time.time() * 1000)))
        self.img1 = 'img/pnumimg1' + millis + '.png'
        plt.savefig(address + '/static/' + self.img1, bbox_inches='tight')  # 保证图片保存完整
        # plt.show()

        plt.figure()
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        labels = []
        sizes = []
        num = 0
        for i in dishes_tup[::-1][:15]:
            labels.append(i[0])
            sizes.append(i[1])
            num += i[1]
        # print(labels, sizes)
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=150)
        plt.title("饼图示例-销量后十五，共占总额%s%%" % str(num * 100 // int(allnum)))
        millis = str(int(round(time.time() * 1000)))
        self.img2 = 'img/pnumimg2' + millis + '.png'
        plt.savefig(address + '/static/' + self.img2, bbox_inches='tight')  # 保证图片保存完整
        # plt.show()

    def order(self):
        # order_info = pd.read_excel('order_info.xlsx')
        # print(order_info)
        number_consumers = self.order_info['number_consumers']
        expenditure = self.order_info['expenditure']
        dishes_count = self.order_info['dishes_count']
        use_start_time = self.order_info['use_start_time']
        use_end_time = self.order_info['use_end_time']

        # 平均消费
        avgcount = str(int(expenditure.mean())) + '元'
        # 人均消费
        menavg = str(expenditure.sum() // number_consumers.sum()) + '元'
        # 平均菜价
        dishe_avg = str(expenditure.sum() // dishes_count.sum()) + '元'
        # 就餐时长
        use_time = use_end_time.values - use_start_time.values
        use_time = use_time.mean()
        use_time //= 60000000000
        use_time = str(use_time).split(' ')[0] + 'min'
        # print(use_time)  # 分钟
        # 日客流量
        datex = []
        humy = []
        dayinfo = self.order_info.set_index('use_start_time')
        year = str(use_start_time[0].year)
        month = str(use_start_time[0].month) if use_start_time[0].month >= 10 else '0' + str(use_start_time[0].month)
        for i in range(use_start_time[0].day, use_start_time[len(use_start_time) - 1].day + 1):
            day = str(i) if i >= 10 else '0' + str(i)
            dayinit = year + '-' + month + '-' + day
            # week
            week = datetime.datetime.strptime(dayinit, "%Y-%m-%d").weekday() + 1
            # print(week)
            day01 = dayinfo[dayinit]
            count = day01['number_consumers'].sum()
            datex.append(dayinit + " 周%d" % week)
            humy.append(count)

        plt.figure()
        plt.rcParams['font.sans-serif'] = ['simhei']  # 用来正常显示中文标签
        x = datex
        y = humy
        # print(x)
        # print(y)
        plt.bar(x, y)
        # 旋转标签
        plt.xticks(rotation=270)
        plt.xlabel('日期/星期')
        plt.ylabel("人数")
        plt.title('日客流量')
        # 标注数字
        for a, b in zip(x, y):
            plt.text(a, b + 0.05, '%d' % b, ha='center', va='bottom', fontsize=11)
        # plt.savefig('../static/img/pnum.png')

        millis = str(round(time.time()))
        self.img3 = 'img/pnumimg3' + millis + '.png'
        plt.savefig(address + '/static/' + self.img3, bbox_inches='tight')  # 保证图片保存完整
        # plt.show()
        self.avgcount = avgcount
        self.menavg = menavg
        self.dishe_avg = dishe_avg
        self.use_time = use_time

    def getdata(self):
        item = {}
        try:
            self.deal()
            self.order()
            item['img1'] = self.img1
            item['img2'] = self.img2
            item['img3'] = self.img3
            item['avgcount'] = self.avgcount
            item['menavg'] = self.menavg
            item['dishe_avg'] = self.dishe_avg
            item['use_time'] = self.use_time
            print(item)
            return item
        except:
            return item



def deal(dishes_info, order_info):

    # dishes_info = pd.read_excel(dishes_url)
    # order_info = pd.read_excel(order_url)
    dishes_info = pd.read_excel(address + "/static/" + dishes_info)
    order_info = pd.read_excel(address + "/static/" + order_info)

    d = DataProcess(dishes_info, order_info)
    return d.getdata()
