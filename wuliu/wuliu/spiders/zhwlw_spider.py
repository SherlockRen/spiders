import scrapy
from scrapy.selector import Selector
from wuliu.items import ZhwlwItem 

class ZhwlwSpider(scrapy.Spider):
    name = "zhwlw"
    allowed_domains = ["www.zhwlw.com.cn"]
    start_urls = []
    for i in range(1, 170):
        start_urls.append("http://www.zhwlw.com.cn/mingpian/Default.asp?id=&key=&PageNo=%d" % i)

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//*[@id="table1"]')
        items = []

        for site in sites:
            item = ZhwlwItem()
            item['name'] = site.xpath('tr[1]/td/p/b/text()').extract()
            item['address'] = site.xpath('tr[3]/td/text()').extract()
            item['telephone'] = site.xpath('tr[4]/td[1]/text()').extract()
            item['phone'] = site.xpath('tr[4]/td[2]/text()').extract()
            item['email'] = site.xpath('tr[5]/td/text()').extract()
            items.append(item)

        return items
