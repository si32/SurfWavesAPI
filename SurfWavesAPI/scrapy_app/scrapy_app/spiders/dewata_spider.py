import scrapy
from scrapy.spiders import Spider


class DewataSpider(Spider):
    name = 'dewata_spider'
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_app.pipelines.DewataItemPipeline': 400,
        },
    }

    start_urls = ['https://www.surf-forecast.com/breaks/Dewata/forecasts/latest']

    def parse(self, response):
        td_data_cell = response.css('td[class="forecast-table__cell forecast-table-wave-height__cell"]')
        raw_data = td_data_cell.css('td::attr(data-swell-state)').get()

        return {"raw_data": raw_data}
