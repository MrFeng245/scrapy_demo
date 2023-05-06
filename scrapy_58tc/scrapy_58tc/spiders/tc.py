import scrapy


class TcSpider(scrapy.Spider):
	name = "tc"
	allowed_domains = ["cn.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify_E%2Cuuid_e5RcpmWYmZeBz48DDJa4nGpyEGE84PMM&search_uuid=e5RcpmWYmZeBz48DDJa4nGpyEGE84PMM&search_type=history"]
	start_urls = ["https://cn.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify_E%2Cuuid_e5RcpmWYmZeBz48DDJa4nGpyEGE84PMM&search_uuid=e5RcpmWYmZeBz48DDJa4nGpyEGE84PMM&search_type=history"]

	def parse(self, response):
		span = response.xpath('//div[@id="filter"]//div[@class="tabs"]/a/span')
		print('=======================================')
		print(span)
