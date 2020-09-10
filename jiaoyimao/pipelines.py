# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import jiaoyimao.settings as settings

class JsonWriterPipeline:
    def __init__(self):
        # 参数初始化，可选实现
        self.file = open(settings.ROOT_PATH + "good.json", 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line.encode('utf-8'))
        self.file.flush()
        return item

    def close_spider(self, spider):
        # 可选实现，当spider被关闭时，这个方法被调用
        self.file.close()
