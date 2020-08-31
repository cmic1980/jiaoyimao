import scrapy
import json
import time
from jiaoyimao.items import JiaoyimaoItem


class SpJiaoYiMao(scrapy.Spider):
    name = "sp_jiaoyimao"
    allowed_domains = ["m.jiaoyimao.com"]
    start_urls = ['https://m.jiaoyimao.com']

    root_url = 'https://m.jiaoyimao.com/fe/ajax/goods/?gameId=9207&cId=1&r=8&extConditions={"lowerPrice":"1000","higherPrice":"3000"}&page='

    def __init__(self):
        pass

    def parse(self, response):
        for i in range(125):
            page = i + 1
            url = self.root_url + str(page)
            time.sleep(5)
            yield scrapy.Request(url=url, callback=self.parse_list)

    def parse_list(self, response):
        body = response.body.decode('utf-8')
        json_object = json.loads(body)
        data = json_object["data"]
        goodList = data["goodsList"]

        for good in goodList:
            item = JiaoyimaoItem()
            item["id"] = good["goodsId"]
            item["title"] = good["realTitle"]
            item["server_name"] = good["serverName"]
            item["category_name"] = good["categoryName"]
            item["price"] = good["price"]

            if good.get("goodsFavoriteCount") != None:
                item["favorite_count"] = good.get("goodsFavoriteCount")
            else:
                item["favorite_count"] = 0

            yield item
