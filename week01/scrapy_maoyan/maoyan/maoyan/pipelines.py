# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv


class MaoyanPipeline:
    def process_item(self, item, spider):
        fname = item['film_name']
        ftype = item['film_type']
        ftime = item['plan_date']
        with open('./movie.csv', 'a+', encoding='utf-8', newline='') as movie:
            writer = csv.writer(movie, dialect='excel')
            writer.writerow([fname, ftype, ftime])
        # mm = pd.DataFrame(data=[fname, ftype, ftime])#,columns=['电影名字','电影类型','上映日期'],index=range(1,11)
        # mm.to_csv('./movie.csv',encoding='utf-8',mode='a+')
        return item