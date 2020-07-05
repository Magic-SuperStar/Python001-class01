# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv

from itemadapter import ItemAdapter


class MaoyanPipeline:
    def process_item(self, item, spider):
        fname = item['film_name']
        ftype = item['film_type']
        ftime = item['plan_date']
        with open('./movie.csv', 'a+', encoding='utf-8', newline='') as movie:
            writer = csv.writer(movie, dialect='excel')
            writer.writerow([fname, ftype, ftime])
        return item
