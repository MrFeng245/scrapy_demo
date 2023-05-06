'''
本例涉及图片下载
多管道下载
多页面访问
'''
import scrapy
from dangdang.items import DangdangItem


class DangSpider(scrapy.Spider):
	name = "dang"
	allowed_domains = ["search.dangdang.com"]
	start_urls = ["http://search.dangdang.com/?key=%B0%A2%BC%D3%C9%AF%BF%CB%C0%EF%CB%B9%B5%D9"]

	base_url = 'http://search.dangdang.com/?key=%B0%A2%BC%D3%C9%AF%BF%CB%C0%EF%CB%B9%B5%D9&act=input%24page_index&page_index='
	page = 1
	
	
	def parse(self, response):
		# piplines 下载数据
		# items	定义数据结构
		# src = //ul[@id="component_59"]/li//img/@src
		# name = //ul[@id="component_59"]/li/a/@title
		# price = //ul[@id="component_59"]/li//p[@class="price"]/span[1]/text()
		# 所有的select对象都可以再调用xpath
		li_list = response.xpath('//ul[@id="component_59"]/li')
		
		for li in li_list:
			# 第一张图片没有懒加载
			src = li.xpath('.//img/@data-original').extract()
			if not src:
				src = li.xpath('.//img/@src').extract()
			
			name = li.xpath('./a/@title').extract()
			price = li.xpath('.//p[@class="price"]/span[1]/text()').extract()
			
			'''
			# 替换不合法的字符文件（/ \ : * " < > | ？）
			str_valid = '（/ \ : * " < > | ？）'
			for i in range(len(name[0])):
				if name[0][i] in str_valid:
					print(name[0][i])
					name[0] = name[0].replace(name[0][i], '')
			'''
			
			# 创建一个DangDangItem对象
			book = DangdangItem(src=src, name=name, price=price)
			# 生成一个book交给piplines下载
			yield book
			
		if self.page < 100:
			self.page += 1
		
			url = self.base_url + str(self.page)
			# 调用parse方法
			# scrapy.Request就是调用scrapy的get请求
			# url:请求地址 callback：要执行的函数
			yield scrapy.Request(url=url, callback=self.parse)
