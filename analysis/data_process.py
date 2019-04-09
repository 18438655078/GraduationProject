import pandas as pd
import numpy as np
import datetime
from matplotlib import pyplot as plt

# 表格数据包括每日菜品名称、价格、被点的次数、每个订单花费、每个订单人数、就餐时间段、
# Avgcount = Menavg = Dishe_avg = Use_time = None


def deal(dishes_info):
    # dishes_info = pd.read_excel('dishes_info.xlsx')
    dishe_name = dishes_info['dishes_name']
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
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    labels = []
    sizes = []
    for i in dishes_tup[:15]:
        labels.append(i[0])
        sizes.append(i[1])
    labels.append('其他')
    sizes.append(allnum)
    print(labels, sizes)
    explode = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', shadow=False, startangle=150)
    plt.title("饼图示例-销量前十五")
    plt.savefig('../static/img/no15.jpg')
    plt.show()

    plt.figure()
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    labels = []
    sizes = []
    num = 0
    for i in dishes_tup[::-1][:15]:
        labels.append(i[0])
        sizes.append(i[1])
        num += i[1]
    print(labels, sizes)
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=150)
    plt.title("饼图示例-销量后十五，共占总额%d%" % num * 100 // int(allnum))
    plt.savefig('../static/img/out15.jpg')
    plt.show()


def order(order_info):
    # order_info = pd.read_excel('order_info.xlsx')
    # print(order_info)
    number_consumers = order_info['number_consumers']
    expenditure = order_info['expenditure']
    dishes_count = order_info['dishes_count']
    use_start_time = order_info['use_start_time']
    use_end_time = order_info['use_end_time']

    # 平均消费
    avgcount = int(expenditure.mean())
    # 人均消费
    menavg = expenditure.sum() // number_consumers.sum()
    # 平均菜价
    dishe_avg = expenditure.sum() // dishes_count.sum()
    # 就餐时长
    use_time = use_end_time.values - use_start_time.values
    use_time = use_time.mean()
    use_time //= 60000000000
    use_time = str(use_time).split(' ')[0] + 'min'
    # print(use_time)  # 分钟
    # 日客流量
    day_hum = {}
    dayinfo = order_info.set_index('use_start_time')
    year = str(use_start_time[0].year)
    month = str(use_start_time[0].month) if use_start_time[0].month >= 10 else '0' + str(use_start_time[0].month)
    for i in range(use_start_time[0].day, use_start_time[len(use_start_time) - 1].day + 1):
        day = str(i) if i >= 10 else '0' + str(i)
        dayinit = year + '-' + month + '-' + day

        # week
        week = datetime.datetime.strptime(dayinit, "%Y-%m-%d").weekday() + 1
        print(week)
        day01 = dayinfo[dayinit]
        count = day01['number_consumers'].sum()
        day_hum[dayinit + " 周%d" % week] = count
        print(day01)
        print('next')
    # print(day_hum)

    plt.figure()
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

    plt.bar(day_hum.keys(), day_hum.values())
    # 旋转标签
    plt.xticks(rotation=270)
    plt.xlabel('日期/星期')
    plt.ylabel("人数")
    plt.title('日客流量')
    # 标注数字
    for a, b in zip(day_hum.keys(), day_hum.values()):
        plt.text(a, b + 0.05, '%d' % b, ha='center', va='bottom', fontsize=11)
    plt.savefig('../static/img/pnum.jpg')
    plt.show()
    # print(avgcount, menavg, dishe_avg, use_time)
    global Avgcount
    global Menavg
    global Dishe_avg
    global Use_time
    Avgcount = avgcount
    Menavg = menavg
    Dishe_avg = dishe_avg
    Use_time = use_time


def get_avgcount():
    return Avgcount


def get_menavg():
    return Menavg


def get_dishe_avg():
    return Dishe_avg


def get_use_time():
    return Use_time


def draw(order_info, dishes_info):
    deal(dishes_info)
    order(order_info)
