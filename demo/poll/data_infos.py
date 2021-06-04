import pandas as pd

class info:
    def citys(self):
        df = pd.read_excel('D:\\code\\untitled3\\bishe\\谷世一\\demos\\demo\\poll\\zufang.xlsx')
        print(df.price.mean())
        city = dict(df.groupby('city').price.count())
        # # city_mean = dict(df.groupby('city').price.mean())
        # # res = [int(i) for i in list(city_mean.values())]
        # # bj = df.loc[df.city == '广州'].groupby('types').city.count()
        # # print(bj.groupby('fuel').name.count())
        # # print(bj)
        # print(city)
        sums = list(city.values())
        names = list(city.keys())
        return names,sums
if __name__ == '__main__':
    info().citys()