# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# Dewata_spider
from itemadapter import ItemAdapter
from main.models import DewataItem
import json
from datetime import date


class DewataItemPipeline():
    def __init__(self):
        self.items = []


    def process_item(self, item, spider):
        self.items.append(item)
        return item


    def close_spider(self, spider):
        # Check if data has already exist
        try:
            DewataItem.objects.filter(date=date.today()).get()
        except DewataItem.MultipleObjectsReturned:
            pass
        except DewataItem.DoesNotExist:
            for j in self.items:
                item = DewataItem()
                i = json.loads(j['raw_data'])
                swell1_height = json.dumps(i[0]['height'], ensure_ascii=False).encode('utf8')
                item.swell1_height = swell1_height.decode()
                swell1_period = json.dumps(i[0]['period'], ensure_ascii=False).encode('utf8')
                item.swell1_period = swell1_period.decode()

                swell2_height = json.dumps(i[1]['height'], ensure_ascii=False).encode('utf8')
                item.swell2_height = swell2_height.decode()
                swell2_period = json.dumps(i[1]['period'], ensure_ascii=False).encode('utf8')
                item.swell2_period = swell2_period.decode()
                swell3_height = json.dumps(i[2]['height'], ensure_ascii=False).encode('utf8')
                item.swell3_height = swell3_height.decode()
                swell3_period = json.dumps(i[2]['period'], ensure_ascii=False).encode('utf8')
                item.swell3_period = swell3_period.decode()
                item.save()
