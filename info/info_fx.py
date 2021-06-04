import pandas as pd
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import GeoType
import matplotlib.pyplot as plt
import seaborn
import numpy as np

g = Geo()

# 租房数据分析过程
class InFo:

    def __init__(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        # seaborn.set(font='SimHei')  # 解决Seaborn中文显示问题
        self.df = pd.read_excel('data/zufang.xlsx')
        print(self.df.head())
        # 自定义分段 color 可以用取色器取色
        self.pieces = [
            {'max': 3000, 'label': '3000以下', 'color': '#50A3BA'},
            {'min': 3000, 'max': 4500, 'label': '3000-4500', 'color': '#3700A4'},
            {'min': 4500, 'max': 6000, 'label': '4500-6000', 'color': '#81AE9F'},
            {'min': 6000, 'max': 7000, 'label': '6000-7000', 'color': '#E2C568'},
            {'min': 7000, 'max': 8000, 'label': '7000-8000', 'color': '#FCF84D'},
            {'min': 8000, 'max': 9000, 'label': '8000-9000', 'color': '#DD0200'},
            {'min': 9000, 'max': 10000, 'label': '9000-10000', 'color': '#DD675E'},
            {'min': 10000, 'label': '10000以上', 'color': '#D94E5D'}  # 有下限无上限
        ]

    # 是否开启seaborn
    def seaborns(self,flag):
        if flag:
            seaborn.set()

    # #######################地图绘制start############################
    def maps(self,city_data,city_name):
        s_list = list(city_data.index)
        geo_cities_coords = {i: [city_data.loc[i]['longitude'], city_data.loc[i]['latitude']] for i in
                             range(s_list[0], s_list[-1])}
        info = []
        g.add_schema(maptype=city_name)
        for i in geo_cities_coords:
            name = city_data.loc[i]['name']
            months = int(city_data.loc[i]['price'])
            tps = (name, months)
            info.append(tps)
        for key in geo_cities_coords:
            # 经度
            lon = geo_cities_coords[key][0]
            # 维度
            lat = geo_cities_coords[key][1]
            name = city_data.loc[key]['name']
            # 定义坐标对应的名称，添加到坐标库中 add_coordinate(name, lng, lat)
            g.add_coordinate(name, lon, lat)
            # 将数据添加到地图上
        g.add('', data_pair=info, type_=GeoType.EFFECT_SCATTER, symbol_size=5)
        # 设置样式
        g.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        #  is_piecewise 是否自定义分段， 变为true 才能生效
        g.set_global_opts(
            visualmap_opts=opts.VisualMapOpts(is_piecewise=True, pieces=self.pieces),
            title_opts=opts.TitleOpts(title="{}-房源分布".format(city_name)),
        )
        # 渲染成html, 可用浏览器直接打开
        g.render('htmls/{}_render.html'.format(city_name))
        print('生成{}的地图文件....'.format(city_name))

    # 北京地区坐标展示
    def bj_info(self):
        name = '北京'
        bj = self.df.loc[self.df.city == name]
        self.maps(bj,name)

    # 上海地区坐标密度展示
    def sh_info(self):
        name = '上海'
        sh = self.df.loc[self.df.city == name]
        self.maps(sh, name)

    # 广州地区坐标展示
    def gz_info(self):
        name = '广州'
        gz = self.df.loc[self.df.city == name]
        self.maps(gz, name)
    # 深圳地区坐标展示
    def sz_info(self):
        name = '深圳'
        sz = self.df.loc[self.df.city == name]
        self.maps(sz, name)
    #######################地图绘制end######################
    ########################### 价格信息总览start#########################
    def detail_info(self):
        plt.figure()
        # 城市房产数据统计柱状图展示
        plt.subplot(2,2,1)
        city_info = dict(self.df.groupby('city').name.count())
        citys = list(city_info.keys())
        citys_counts = list(city_info.values())
        plt.bar(citys,citys_counts,color='rgb')
        plt.xlabel('城市名称')
        plt.ylabel('租房数量')
        plt.title('城市数量一览')

        # 城市租房总价格
        plt.subplot(2,2,2)
        city_info_price = dict(self.df.groupby('city').price.sum())
        plt.bar(list(city_info_price.keys()), list(city_info_price.values()), color='rgb')
        plt.xlabel('城市名称')
        plt.ylabel('租房总价格')
        plt.title('城市租房月总价格')

        # 城市租房价格平均价格
        plt.subplot(2, 2, 3)
        city_info_mprice = dict(self.df.groupby('city').price.mean())
        print(city_info_mprice)
        plt.bar(list(city_info_mprice.keys()), list(city_info_mprice.values()), color='rgb')
        plt.xlabel('城市名称')
        plt.ylabel('租房平均价格')
        plt.title('城市租房月平均价格')

        # 租金价格与经纬度的关系散点图
        plt.subplot(2,2,4)
        x = self.df.latitude * 1000
        y = self.df.longitude * 1000
        s = self.df.price * 0.001
        plt.scatter(x,y,alpha=0.1,s=s,c=self.df.price* 0.01)
        plt.xlabel('城市经度')
        plt.ylabel('城市维度')
        plt.title('城市经纬度与价格关系图')
        # plt.legend()
        plt.show()
    ################################价格信息end###########################

    ##############房屋面积信息start###################
    def areas(self):
        # 开关
        # self.seaborns(True)
        grid = plt.GridSpec(3, 5, wspace=0.4, hspace=0.9)
        # 面积折线图
        plt.subplot(grid[0,:2])
        areas = self.df.groupby('area').city.count()
        area_dict = dict(areas)
        # 面积
        area_key = area_dict.keys()
        area_values = area_dict.values()
        # 饼状图实现
        plt.plot(list(area_key),list(area_values),color='b')
        plt.xlabel('面积')
        plt.ylabel('数量')
        plt.title('城市面积折线图')

        # 柱状图
        plt.subplot(grid[0,2:])
        plt.bar(list(area_key),list(area_values),color='b')
        plt.xlabel('面积')
        plt.ylabel('数量')
        plt.title('城市面积柱状图')

        # 折线图
        plt.subplot(grid[1,:])
        # plt.axis('equal')
        self.df.loc[self.df.city == '北京'].groupby('area').city.count().plot(label='北京')
        self.df.loc[self.df.city == '上海'].groupby('area').city.count().plot(label='上海')
        self.df.loc[self.df.city == '广州'].groupby('area').city.count().plot(label='广州')
        self.df.loc[self.df.city == '深圳'].groupby('area').city.count().plot(label='深圳')
        plt.xlabel('面积')
        plt.ylabel('数量')
        plt.title('各城市面积折线图')
        plt.xlim(0,400)

        # plt.xlim(0,300)

        # 面积与价格散点图
        rng = np.random.RandomState(0)
        plt.subplot(grid[2,:])
        x = self.df['price']
        colors = rng.rand(len(x))
        y = self.df.area
        plt.scatter(x,y,alpha=0.3,s=5,c=colors)
        plt.xlabel('月租金')
        plt.ylabel('面积')
        plt.title('各城市面积散点图')
        plt.xlim(0, 10000)
        plt.ylim(0,400)

    ##############房屋面积信息end###################

    ##############房屋信息start################
    def house_info(self):
        # 是否有燃气
        x = dict(self.df.groupby('fuel').price.count())
        explode = (0, 0.1)
        labels = list(x.keys())
        del labels[1]
        x = list(x.values())
        del x[1]
        plt.pie(x, explode=explode,labels=labels, autopct='%1.1f%%', shadow=True, startangle=150)
        plt.title("房源燃气信息占比")
    # 各个地区的燃气情况
    def area_fuel(self):
        plt.figure()
        plt.subplot(2,2,1)
        # 北京地区
        bj = self.df.loc[self.df.city == '北京']
        x = list(dict(bj.groupby('fuel').price.count()).values())
        del x[1]
        y = list(dict(bj.groupby('fuel').price.count()).keys())
        del y[1]
        explode = (0, 0.1)
        plt.pie(x, explode=explode, labels=y, autopct='%1.1f%%', shadow=True, startangle=150)
        plt.title("北京地区房源燃气信息占比")
        plt.subplot(2, 2, 2)
        # 上海地区
        bj = self.df.loc[self.df.city == '上海']
        x = list(dict(bj.groupby('fuel').price.count()).values())
        del x[1]
        y = list(dict(bj.groupby('fuel').price.count()).keys())
        del y[1]
        explode = (0, 0.1)
        plt.pie(x, explode=explode, labels=y, autopct='%1.1f%%', shadow=True, startangle=150)
        plt.title("上海地区房源燃气信息占比")
        plt.subplot(2, 2, 3)
        # 广州地区
        bj = self.df.loc[self.df.city == '广州']
        x = list(dict(bj.groupby('fuel').price.count()).values())
        del x[1]
        y = list(dict(bj.groupby('fuel').price.count()).keys())
        del y[1]
        explode = (0, 0.1)
        plt.pie(x, explode=explode, labels=y, autopct='%1.1f%%', shadow=True, startangle=150)
        plt.title("广州地区房源燃气信息占比")
        plt.subplot(2, 2, 4)
        # 北京地区
        bj = self.df.loc[self.df.city == '深圳']
        x = list(dict(bj.groupby('fuel').price.count()).values())
        del x[1]
        y = list(dict(bj.groupby('fuel').price.count()).keys())
        del y[1]
        explode = (0, 0.1)
        plt.pie(x, explode=explode, labels=y, autopct='%1.1f%%', shadow=True, startangle=150)
        plt.title("深圳地区房源燃气信息占比")

    # 是否有电梯
    def house_dt(self):
        # 是否有电梯
        x = dict(self.df.groupby('elevator').price.count())
        explode = (0, 0.1)
        labels = list(x.keys())
        del labels[1]
        x = list(x.values())
        del x[1]
        plt.pie(x, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=150)
        plt.title("房源电梯信息占比")
    def city_housedt(self):
        plt.figure()
        plt.subplot(2, 2, 1)
        # 北京地区
        bj = self.df.loc[self.df.city == '北京']
        x = list(dict(bj.groupby('elevator').price.count()).values())
        y = list(dict(bj.groupby('elevator').price.count()).keys())
        explode = (0, 0.1)
        plt.pie(x, explode=explode, labels=y, autopct='%1.1f%%', shadow=True, startangle=150)
        plt.title("北京地区房源电梯信息占比")
        plt.subplot(2, 2, 2)
        # 上海地区
        bj = self.df.loc[self.df.city == '上海']
        x = list(dict(bj.groupby('elevator').price.count()).values())
        y = list(dict(bj.groupby('elevator').price.count()).keys())
        explode = (0, 0.1)
        plt.pie(x, explode=explode, labels=y, autopct='%1.1f%%', shadow=True, startangle=150)

        plt.title("上海地区房源电梯信息占比")
        plt.subplot(2, 2, 3)
        # 广州地区
        bj = self.df.loc[self.df.city == '广州']
        x = list(dict(bj.groupby('elevator').price.count()).values())
        y = list(dict(bj.groupby('elevator').price.count()).keys())
        del x[1]
        del y[1]
        explode = (0, 0.1)
        plt.pie(x, explode=explode, labels=y, autopct='%1.1f%%', shadow=True, startangle=150)
        plt.title("广州地区房源电梯信息占比")

        plt.subplot(2, 2, 4)
        # 深圳地区
        bj = self.df.loc[self.df.city == '深圳']
        x = list(dict(bj.groupby('elevator').price.count()).values())
        y = list(dict(bj.groupby('elevator').price.count()).keys())
        explode = (0, 0.1)
        plt.pie(x, explode=explode, labels=y, autopct='%1.1f%%', shadow=True, startangle=150)
        plt.title("深圳地区房源电梯信息占比")
    ##############房屋信息end#################

    ##############房型信息start###############
    def types(self):
        types = self.df.groupby('types').price.count()
    ##############房型信息end#################



if __name__ == '__main__':
    info = InFo()
    # info.bj_info()
    # info.sh_info()
    # info.detail_info()
    # info.gz_info()
    # info.sz_info
    # info.areas()
    # 绘图库出图
    # plt.legend()
    # info.house_info()
    # info.area_fuel()
    # info.house_dt()
    # info.city_housedt()
    info.types()
    plt.show()





