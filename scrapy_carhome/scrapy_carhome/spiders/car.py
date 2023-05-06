import scrapy


class CarSpider(scrapy.Spider):
	name = "car"
	allowed_domains = ["car.autohome.com.cn/price/brand-33.html"]
	# 如果请求接口以html结尾，不加'/'
	start_urls = ["https://car.autohome.com.cn/price/brand-33.html"]
    
	def parse(self, response):
		print('======================')
		name_list = response.xpath('//div[@class="main-title"]/a/text()')
		price_list = response.xpath('//span[@class="font-arial"]/text()')
		for i in range(len(name_list)):
			name = name_list[i].extract()
			price = price_list[i].extract()
			print(name, price)
