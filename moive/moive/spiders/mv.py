'''
本例涉及页面的跳转
定义新的处理页面逻辑的方法
yield向另一个方法传参
'''
import scrapy
from moive.items import MoiveItem


class MvSpider(scrapy.Spider):
	name = "mv"
	allowed_domains = ["dytt8.net"]
	start_urls = ["https://dytt8.net/index2.htm"]

	def parse(self, response):
		# 第一个名字和第二页的图片
		# name = //div[@class="co_area2"]//td[1]/a[2]/text()
		# src = //div[@class="co_area2"]//td[1]/a[2]/@href
		a_list = response.xpath('//div[@class="co_area2"]//td[1]/a[2]')
		print('=================================================')
		for a in a_list:
			name = a.xpath('./text()').extract_first()
			src = a.xpath('./@href').extract_first()
			
			# 第二页的地址
			url = f'https://dytt8.net/{src}'
			# 对第二页发起访问
			# meta传递参数
			yield scrapy.Request(url=url, callback=self.parse_second, meta={'name': name})
			
	def parse_second(self, response):
		# span标签识别不了[首先检查xpath]
		src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
		# 接受到请求的mate参数值
		name = response.meta['name']
		
		moive = MoiveItem(src=src, name=name)
		yield moive
