# https://bj.lianjia.com/zufang/
# https://sh.lianjia.com/zufang/
# https://gz.lianjia.com/zufang/
# https://sz.lianjia.com/zufang/
# pg1/#contentList
import requests
import xlwt
from lxml import etree
import re


class spider_zf:
    def __init__(self, city):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
        self.base_url = ''
        self.city = city
        self.index = 0
        self.wb = xlwt.Workbook()
        self.ws = self.wb.add_sheet('zufang')
        self.write_csv('name', 'price', 'types', 'area', 'floor', 'elevator', 'fuel', 'longitude', 'latitude')
        self.longpattern = re.compile(r"longitude: '(.*)'")
        self.latpattern = re.compile(r"latitude: '(.*)'")

    def go_city(self):
        for i in self.city:
            flag = True
            while flag:
                try:
                    self.base_url = 'https://' + i + '.lianjia.com'
                    self.go_homel(self.base_url + '/zufang/pg{}/#contentList')
                    print(i, 'is ok')
                    flag = False
                except Exception as e:
                    print(e)
        self.wb.save('zufang.csv')

    def go_homel(self, url):
        for i in range(1, 101):
            flag = True
            while flag:
                try:
                    reponse = requests.get(url.format(i), headers=self.headers)
                    html = etree.HTML(reponse.text)
                    homelist = html.xpath("//a[@class='twoline']/@href")
                    self.spider_home(homelist)
                    print(i, '页 is ok')
                    flag = False
                except Exception as e:
                    print(e)

    def spider_home(self, homelist):
        for i in homelist:
            flag = True
            while flag:
                try:
                    reponse = requests.get(self.base_url + i, headers=self.headers)
                    html = etree.HTML(reponse.text)
                    name = html.xpath("//p[@class='content__title']/text()")[0].split('·')[-1].split(' ')[0]
                    price = float(html.xpath("//div[@class='content__aside--title']/span/text()")[0])
                    types_area = html.xpath("//ul[@class='content__aside__list']/li[2]/text()")[0].split(' ')
                    types = types_area[0]
                    area = float(types_area[1].replace('㎡', ''))
                    floor = html.xpath("//li[@class='fl oneline'][8]/text()")[0].split('：')[-1]
                    elevator = html.xpath("//li[@class='fl oneline'][9]/text()")[0].split('：')[-1]
                    fuel = html.xpath("//li[@class='fl oneline'][15]/text()")[0].split('：')[-1]
                    longitude = float(self.longpattern.findall(reponse.text)[0])
                    latitude = float(self.latpattern.findall(reponse.text)[0])
                    self.write_csv(name, price, types, area, floor, elevator, fuel, longitude, latitude)
                    flag = False
                except Exception as e:
                    print(e)

    def write_csv(self, name, price, types, area, floor, elevator, fuel, longitude, latitude):
        self.ws.write(self.index, 0, name)
        self.ws.write(self.index, 1, price)
        self.ws.write(self.index, 2, types)
        self.ws.write(self.index, 3, area)
        self.ws.write(self.index, 4, floor)
        self.ws.write(self.index, 5, elevator)
        self.ws.write(self.index, 6, fuel)
        self.ws.write(self.index, 7, longitude)
        self.ws.write(self.index, 8, latitude)
        self.index += 1
        # print(self.index, name, '行 is ok')


if __name__ == '__main__':
    spider = spider_zf(['bj', 'sh', 'sz', 'gz'])
    spider.go_city()
