# -*- coding: utf-8 -*-
"""
author: LJZ
time: 2020/7/21 11:46

"""
import pymysql
from twisted.enterprise import adbapi
from scrapy.utils.project import get_project_settings
import time


class DBHelper(object):
    '''读取settings中的配置，自行修改代码进行操作'''

    def __init__(self):
        # 获取settings配置，设置需要的信息
        settings = get_project_settings()
        dbparams = dict(host=settings['MYSQL_HOST'],
                        db=settings['MYSQL_NAME'],
                        passwd=settings['MYSQL_PASSWORD'],
                        charset=settings['MYSQL_CHARSET'],
                        cursorclass=pymysql.cursors.DictCursor,
                        use_unicode=False)
        # **表示将字典扩展为关键字参数，相当于host=xxx,db=yyy....
        # 指定操作数据库的模块名和数据库参数
        self.dbpool = adbapi.ConnectionPool('pymysql', **dbparams)

    def connect(self):
        return self.dbpool

    # 插入数据
    # 使用twisted将mysql插入变成异步执行
    def insert(self, item):
        sql = 'INSERT INTO film ( film_name, film_type, plan_date, conect_url, create_date ) VALUES ( % s,% s,% s,% s,% s )'
        # 调入插入的方法
        # 指定操作方法与操作数据
        query = self.dbpool.runInteraction(self._conditional_insert, sql, item)
        # 调用异常处理方法
        query.addErrback(self._handle_error)

    # 写入数据库中
    def _conditional_insert(self, tx, sql, item):
        locltime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        params = (
        item['film_name'], item['film_type'], item['plan_date'], item['connect_url'], locltime)
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        tx.execute(sql, params)
    # 错误处理方法
    def _handle_error(self, failue):
        print('------------------------database operation exception!!------------------------')
        print(failue)
