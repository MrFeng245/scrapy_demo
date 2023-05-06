import scrapy


class BaiduSpider(scrapy.Spider):
	# 爬虫的名字 用于运行爬虫时 使用的值
    name = "baidu"
    # 允许访问的域名
    allowed_domains = ["www.baidu.com"]
    # 起始的URL地址：第一次要访问的域名
    # start_urls = 'http://' + allowed_domains +'/'
    start_urls = ["http://www.baidu.com/"]

	# 执行了start_url之后 执行的方法 方法中的response 就是返回的那个对象
	# response = urllib.request.urlopen()
	# response = requests.get()
    def parse(self, response):
        print('哈喽')
