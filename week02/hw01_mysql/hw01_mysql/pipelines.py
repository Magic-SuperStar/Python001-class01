# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from hw01_mysql.db.DBHelper import DBHelper


class Hw01MysqlPipeline:
    def __init__(self):
        self.db = DBHelper()

    def process_item(self, item, spider):
        #插入数据
        self.db.insert(item)
        return item
