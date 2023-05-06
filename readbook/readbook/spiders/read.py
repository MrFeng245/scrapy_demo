'''
本例展示crawl spider的基本使用
跟进爬取
'''
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from readbook.items import ReadbookItem


class ReadSpider(CrawlSpider):
	name = "read"
	allowed_domains = ["www.dushu.com"]
	# 使用crawl spider规则，第一页缺失https://www.dushu.com/book/1617.html
	start_urls = ["https://www.dushu.com/book/1617.html"]
	
	# follow：表示是否跟进
	rules = (Rule(LinkExtractor(allow=r"/book/1617(_\d+)?\.html"),
			callback="parse_item", 
			follow=False),)
	

	def parse_item(self, response):
		item = {}
		# 爬取图片/名字/作者
		# src = //div[@class="bookslist"]//div[@class="book-info"]//img/@data-original
		# name = //div[@class="bookslist"]//div[@class="book-info"]//h3/a/text()
		# author = //div[@class="bookslist"]//div[@class="book-info"]//p[1]/text()
		div_list = response.xpath('//div[@class="book-info"]')
		
		for div in div_list:

			src = div.xpath('./div//img/@data-original').extract_first()
			name = div.xpath('./h3/a/text()').extract_first()
			author = div.xpath('./p[1]/text()').extract_first()
			
			book = ReadbookItem(name=name, src=src, author=author)
			yield book
		
		return item
