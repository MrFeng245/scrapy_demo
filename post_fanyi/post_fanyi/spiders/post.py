import scrapy
import json


class PostSpider(scrapy.Spider):
	name = "post"
	allowed_domains = ["fanyi.baidu.com/sug"]
	# 使用post请求的url，start_url和parse请求均失效
	#start_urls = ["https://fanyi.baidu.com/sug"]

	#def parse(self, response):
	#	pass

	def start_requests(self):
		url = 'https://fanyi.baidu.com/sug'
		
		data = {
			'kw': 'look'
		}
		
		yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)
		
	def parse_second(self, response):
		content = response.text
		obj = json.loads(content, encoding='utf-8')
		print(obj)
