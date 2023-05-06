# pipelines.py
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 使用管道：在settings开启管道
class DangdangPipeline:
	def open_spider(self, spider):
		'''在爬虫文件开始之前执行的方法'''
		self.fp = open('book.json', 'w', encoding='utf-8')
	
	
	# item就是yield后面的book对象
	def process_item(self, item, spider):
		# 不推荐以下模式：每传递一个对象，就打开一个文件，IO过于频繁
		# write方法必须接受字符串对象,item是DangDangItem对象
		#with open('book.json', 'a', encoding='utf-8') as fp:
		#	fp.write(str(item))
		
		# 使用打开和关闭函数(方法名只能是那两个，不能改)解决频繁IO的问题
		self.fp.write(str(item))
		return item
		
		
	def close_spider(self, spider):
		'''在爬虫文件执行结束后执行'''
		self.fp.close()
		

from urllib.request import urlretrieve
# 开启多条管道
class DangdangDownloadPipline:
	'''定义管道类'''
	def process_item(self, item, spider):
		url = f'https:{item.get("src")[0]}'
		filename = f'./books/{item.get("name")[0].lstrip()}.jpg'
		# 测试代码
		urlretrieve(url=url, filename=filename)
		return item
