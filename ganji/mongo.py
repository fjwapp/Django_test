#!/usr/bin/env python
# encoding: utf-8

# version: 1.0
# author: fjwapp
# license: Apache Licence 
#获取一部分网站需要的数据
import pymongo

client = pymongo.MongoClient('localhost',27017)
wbsite = client['wbsite']
wbsite_item =wbsite['wbsite_item']
item_info = client['item_info']
item_detail_backup=item_info['item_detail_backup']

for i in item_detail_backup.find().limit(300):

    data = {
        'url':i['url'],
        'address':i['address'],
        'deal_number':i['deal_number'],
        'title':i['title'],
        'price':i['price'],
        'person_look_count':i['person look conut']#之前key值写错了 只能这样改了
    }
    print(data)
    wbsite_item.insert_one(data)

# for i in wbsite_item.find():
#     wbsite_item.delete_one({'person look conut':i['person look conut']})
#     print(i)