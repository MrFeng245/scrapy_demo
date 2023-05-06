python爬虫

# <span style="color: cornflowerblue;">预备知识</span>

## <span style="color: orange;">爬虫原理</span>

网络链接：计算机一次`request`请求和服务器端的`response`回应

爬虫：

- 模拟计算机对服务器发起的`request`请求
- 接收服务器端的`response`内容并解析

## <span style="color: orange;">页面结构</span>

```html
<html lang="en">
    <head>
        
    </head>
    <body>
        <!-- table 表格
            tr 行
            td 列
        -->
        <table width="200", height="50">
            <tr>
                <td>列1</td>
                <td>列2</td>
                <td>列3</td>
            </tr>
            <tr>
                <td>李萌</td>
                <td>女</td>
                <ed>34</ed>
            </tr>
        </table>
        <!-- ul li-->
        <ul>
            <li>无序列表（无关联）</li>
        </ul>
        <ol>
            <li>有序列表（有关联）</li>
        </ol>
        <a href="域名">超链接</a>
    </body>
</html>
```

## <span style="color: orange;">反爬手段</span>

- [x] User-Agent：服务器识别客户端的信息
- [x] 代理IP
- [ ] 验证码访问
- [ ] 动态加载网页：页面返回js数据
- [ ] 数据加密

## <span style="color: orange;">http请求方法</span>

- get请求：获取服务器数据
- post请求：向服务器发送数据

# <span style="color: cornflowerblue;">urllib</span>

## <span style="color: orange;">urllib的三步</span>

- 定制请求（Request）
- 获取响应（urlopen）
- read内容（read(), encode）

## <span style="color: orange;">基本使用</span>

### <span style="color: burlywood;">例 | urllib请求源码</span>

> urllib.request.urlopen

```python
from urllib.request import urlopen


url = 'https://cn.bing.com/'
# reponse 的类型为 HTTPResponse
response = urlopen(url)
# 获取响应页面的源码
# read方法返回二进制数据（b''），按字节读，需解码
# read(num) num表示读的字节总数
content = response.read().decode('utf-8')

print('源码：' + content)
```

### <span style="color: burlywood;">response 的6个方法</span>

```python
# 读取二进制码
response.read() # 按字节读
response.readline() # 按行读，只能读一行
response.readlines() # 按行读，只能读一行
# 返回状态码
response.getcode()
# 返回URL地址
response.geturl()
# 获取状态信息
response.getheaders()
```

### <span style="color: burlywood;">urlretrieve下载文件</span>

> urllib.request.urlretrieve

```python
from urllib.request import urlopen
from urllib.request import urlretrieve


# 下载页面
url = 'https://cn.bing.com/'
filename = 'bing首页.html'
urlretrieve(url, filename)

# 下载图片
url_img = 'https://www.mlito.com/wp-content/uploads/2018/03/bf478dbc95-768x1152.jpg'
filename = '女性.jpg'
urlretrieve(url_img, filename)

# 下载音乐
url_music = 'https://webfs.tx.kugou.com/202304291708/2bf051a54656fe2ea96be7fd1693de16/v2/a06b033b356bfc974c5245d0195086a5/KGTX/CLTX001/a06b033b356bfc974c5245d0195086a5.mp3'
filename = '成都.mp3'
urlretrieve(url_music, filename)

# 下载视频
url_video = 'https://kvideo01.youju.sohu.com/49377d8f-bf43-4bdb-879a-fd1fc8baa4a02_0_0.mp4?sign=dc22bf258ef9eb78769c007c500ba1d5&t=1682780515'
filename = 'video.mp4'
urlretrieve(url_video, filename)
```

## <span style="color: orange;">请求对象的定制</span>

> urllib.request.Request

URL的组成

- 协议（http/https）
- 主机（www.baidu.com）
- 端口号(80/443)
- 路径(s)
- 参数(wd=xx)
- 锚点

### <span style="color: burlywood;">headers伪装</span>

```python
# 爬百度主页
from urllib.request import urlopen
from urllib.request import Request


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'
}
url = 'https://www.baidu.com'
# Request方法伪装请求-针对UA反爬
request = Request(url=url, headers=headers)
response = urlopen(request)
content = response.read().decode('utf-8')
print(content)
```

### <span style="color: burlywood;">IP伪装</span>

#### handler处理器

> 定制更高级的请求头（为代理做铺垫）

```python
from urllib.request import Request, urlopen, HTTPHandler, build_opener


url = 'http://cn.bing.com'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'
}

request = Request(url, headers=headers)
# handler build_opener open

# 获取handler对象
handler = HTTPHandler()
# 获取opener对象
opener = build_opener(handler)
# 调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')
print(content)
```

#### 代理服务器

> 使用代理ip实现爬虫

```python
from urllib.request import Request, urlopen, ProxyHandler, build_opener


url = 'http://www.ip111.cn/'
headers = {
    'Referer': 'https://cn.bing.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'
}

request = Request(url, headers=headers)
#response = urlopen(request)
proxies = {
    'http': '47.111.173.88:8888'
}
handler = ProxyHandler(proxies=proxies)
opener = build_opener(handler)
response = opener.open(request)

content = response.read().decode('utf-8')

with open('ip.html', 'w', encoding='utf-8') as f:
    f.write(content)
```

#### 代理池

```python
import random
from urllib.request import Request, ProxyHandler, build_opener


url = 'http://www.ip111.cn/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'
}
proxies_pool = [
    # 此处传入可用ip
    {'http': '47.111.173.88:8888'},
    {'http': '47.111.173.88:888'},
]
proxies = random.choice(proxies_pool)
request = Request(url, headers=headers)

handler = ProxyHandler(proxies=proxies)
opener = build_opener(handler)
response = opener.open(request)

content = response.read.decode('utf-8')

with open('ip.html', 'w', encoding='utf-8') as f:
    f.write(content)
```

## <span style="color: orange;">http请求方法</span>

#### <span style="color: burlywood;">post请求</span>

- 不同于get请求方式，post请求的参数必须编码，调用encode
- 参数放在请求对象定制的方法中

```python
# 爬百度翻译
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode, quote
import json


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'
}
url = 'https://fanyi.baidu.com/sug'
data = {
    'kw':'content'
}

data = urlencode(data).encode('utf-8')
request = Request(url, data, headers)
# post请求的参数是字节型，需要编码
response = urlopen(request)
content = response.read().decode('utf-8')
# 按json对象打印
print(json.loads(content))
```

### <span style="color: burlywood;">ajax两种请求</span>

> Ajax的意思是：**异步JavaScript和XML**。\[`X-Requested-With: XMLHttpRequest`\]
>
> 通俗的理解：在网页中利用**XMLHttpRequest**对象**和服务器进行数据交互**的方式，就是Ajax

#### ajax之get请求

```python
# 找到接口：无需在意数据包的类型，需要找到含内容的数据包，同时确定数据的请求类型（get/post）
# 爬豆瓣某一类型定义的top榜
from urllib.request import Request, urlopen
from urllib.request import Request, urlopen
from urllib.parse import urlencode


def create_request(page):
    '''为page页面定制请求'''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'
    }
    base_url = 'https://movie.douban.com/j/chart/top_list?type=10&interval_id=100%3A90&action=&'
    data = {
        'start':(page - 1) * 20,
        'limit':20
    }
    url = base_url + urlencode(data)
    request = Request(url, headers=headers)
    return request
    
    
def get_content(request):
    '''获取request请求的内容'''
    response = urlopen(request)
    content = response.read().decode('utf-8')
    return content
    

def download(content, page):
    '''把content内容下载到本地'''
    filename = f'douban_{page}.json'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    

def main():
    start_page = int(input('input start page:'))
    end_page = int(input('input end page:'))
    for page in range(start_page, end_page+1):
        # 定制每一页的请求
        request = create_request(page)
        # 获取响应数据
        content = get_content(request)
        # 下载
        download(content, page)

    
if __name__ == '__main__':
    main()
```

#### ajax之post请求

```python
# 网址相同，查看【负载】的【表单数据】
from urllib.request import Request, urlopen
from urllib.parse import urlencode


def create_request(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'
    }
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    
    data = {
        'cname': '北京',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10'
    }
    data = urlencode(data).encode('utf-8')
    request = Request(base_url, data, headers)
    return request
    

def get_content(request):
    response = urlopen(request)
    content = response.read().decode('utf-8')
    return content
    
    
def download(content, page):
    filename = f'kfc_{page}.json'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    start_page = int(input('input start page:'))
    end_page = int(input('input end page:'))
    for page in range(start_page, end_page+1):
        request = create_request(page)
        content = get_content(request)
        download(content, page)
        

if __name__ == '__main__':
    main()
```

## <span style="color: orange;">汉字编码解码</span>

#### urllib.parse.quote

> 包装URL，适用于对少量汉字编码（如1次）

```python
# 爬bing搜索
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import quote


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'
}

def get_code(url):
    request = Request(url=url, headers=headers)
    response = urlopen(request)
    content = response.read().decode('utf-8')
    print(content)


def main():
    '''嵌入bing搜索引擎，获取源码'''
    head = 'https://cn.bing.com/search?q='
    while True:
        keyword = input('input keyword: ')
        if keyword == 'q':
            break
        # quote方法：keyword编码为unicode
        url = head + quote(keyword)
        get_code(url)
    
    
if __name__ == '__main__':
    main()
```

#### urllub.parse.urlencode

> 包装URL，对字典中的内容进行编码并自动形成URL格式

```python
# 爬bing搜索
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'
}

def get_code(url):
    # Request方法伪装请求-针对UA反爬
    request = Request(url=url, headers=headers)
    response = urlopen(request)
    content = response.read().decode('utf-8')
    print(content)


def main():
    head = 'https://cn.bing.com/search?q='
    data = {
        'wd': '毛不易',
        'sex': '男'
    }
    # urlencode方法：编码多个参数，参数：字典
    rear = urlencode(data)
    url = head + rear
    get_code(url)
    
    
if __name__ == '__main__':
    main()
```

## <span style="color: orange;">cookie登录</span>

> 爬虫模拟登录

```python
from urllib.request import Request, urlopen

# 大部分情况下，请求头不够，导致请求失败
headers = {
    # 判断当前路径是否由上一个路径进来的，一般用于图片的防盗链
    'referer': 'https://www.bilibili.com/',
    # 携带登录信息
    'cookie': 'buvid3=8AC41F54-4B24-2870-7985-DD3830B9FFE318361infoc; b_nut=1674891318; CURRENT_FNVAL=4048; _uuid=1010394E3B-13E2-6637-C1C6-6E9355381EBE24194infoc; buvid4=DA568548-E792-D438-18EB-17DFD3F5E77826348-023012815-U0lQNatlIrPT954HQrZgng==; rpdid=|(J~R)uRmRml0J\'uY~R)muR|m; DedeUserID=340488590; DedeUserID__ckMd5=78e600f65428a758; nostalgia_conf=-1; i-wanna-go-back=-1; b_ut=5; header_theme_version=CLOSE; home_feed_column=5; CURRENT_PID=11c00130-ca25-11ed-b9c7-212056d899c4; innersign=0; b_lsid=8EEC7E6F_187D6020B7C; bsource=search_bing; FEED_LIVE_VERSION=V8; browser_resolution=1440-856; SESSDATA=49e5efb9,1698474694,152ba*52; bili_jct=2c18d9a3b800ee515940d08ce80f685c; sid=53vx3val; bp_video_offset_340488590=790635618959884300; fingerprint=41fbec47ebebd41549b300162e3a9460; buvid_fp_plain=undefined; hit-new-style-dyn=0; buvid_fp=41fbec47ebebd41549b300162e3a9460; hit-dyn-v2=1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'
}

url = 'https://space.bilibili.com/340488590/dynamic'

request = Request(url, headers=headers)
response = urlopen(request)
# ctrl+U 查询编码格式
content = response.read().decode('utf-8')

with open('bilibili.html', 'w', encoding='utf-8') as f:
    f.write(content)
```

## <span style="color: orange;">URLError</span>

> HTTPError是URLError的子类
>
> HTTPError:当我们向服务器发出请求时，服务器会产生response请求，如果urlopen不能处理则爆出httperror异常

URLError产生的原因主要是：

1.  网络没有连接
2.  服务器连接失败
3.  找不到指定的服务器

```python
# urllib的两种常用异常
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError


def get_title(url):
    '''通过url返回名称列表'''
    try:
        html = urlopen(url)
    # HTTPError：捕获 服务器未正常响应 的异常
    # URLError：捕获 服务器不存在/URL输入错误 的异常
    except (HTTPError, URLError) as e:
        return None
    try:
        # 创建一个beautifulsoup对象
        soup = BeautifulSoup(html, 'lxml')
        # 用标签属性获取一组标签：用字典把属性传到函数里
        name_list = soup.find_all('span', {'class':'green'})
    # AttributeError：捕获 找不到对象的属性 异常（防止title为空导致程序崩溃）
    except AttributeError as e:
        return None
    return name_list
    
    
def main():
    '''通过属性查找数据'''
    name_list = get_title("https://pythonscraping.com/pages/warandpeace.html")
    if name_list == None:
        print('NameList could not be found')
    else:
        for name in name_list:
            print(name.get_text())


if __name__ == '__main__':
    main()
```

# <span style="color: cornflowerblue;">Requests</span>

> 和request作用一致，操作更简单
>
> 官方文档：https://requests.readthedocs.io/en/latest/
>
> 快速上手：https://requests.readthedocs.io/projects/cn/zh_CN/latest/user/quickstart.html

## <span style="color: orange;">基本使用</span>

### <span style="color: burlywood;">请求源码</span>

```PYTHON
import requests


url = 'https://www.baidu.com'
# Response类型
response = requests.get(url)
# 设置响应的编码格式
response.encoding = 'utf-8'
# 以字符串的形式返回网页的源码
print(response.text)
```

### <span style="color: burlywood;">response的6个属性</span>

```python
# 设置响应的编码格式
response.encoding = 'utf-8'
# 以字符串的形式返回网页的源码
print(response.text)
# 返回一个URL地址
print(response.url)
# 以二进制形式返回网页源码
print(response.content)
# 返回响应的状态码
print(response.status_code)
# 获取响应头
print(response.headers)
```

## <span style="color: orange;">HTTP请求</span>

### <span style="color: burlywood;">get请求</span>

- 参数使用params传递
- 参数资源无需urlencode编码
- 不需要请求对象的定制
- 请求资源路径中的问号可加可不加

```python
import requests

# 请求资源路径中的问号可加可不加 url = 'https://cn.bing.com/search'
url = 'https://cn.bing.com/search?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'
}
data = {
    'q': '北京'
}

# url 请求资源路径
# params 参数 参数使用params传递 参数资源无需urlencode编码
# kwargs 字典
# 不需要请求对象的定制
response = requests.get(url=url, params=data, headers=headers)
content = response.text
print(content)
```

### <span style="color: burlywood;">post请求</span>

- post请求无需编解码
- post请求的参数是data
- 不需要请求对象的定制

```python
import requests
import json


url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'
}
data = {
    'kw': 'look at'
}

# url 资源请求路径
# data 请求参数
# json 
# kwargs 字典
response = requests.post(url=url, data=data, headers=headers)
content = response.text

# 利用json转为中文
obj = json.loads(content, encoding='utf-8')
print(obj)
```

## <span style="color: orange;">代理</span>

```python
import requests


url = 'https://www.baidu.com/s'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'
}
data = {
    'wd': 'ip'
}

proxy = {
    'https': '45.62.169.87:9002'
}

response = requests.get(url=url, params = data, headers=headers, proxies=proxy)
content = response.text
with open('daili.html', 'w', encoding='utf-8') as f:
    f.write(content)
```

## <span style="color: orange;">cookie登录</span>

```python
# 通过登录古诗文网，进入主页面
# 难点：隐藏域、验证码
# 发现__VIEWSTATE，__VIEWSTATEGENERATOR在页面源码中，获取解析即可
# 下载验证码，输入
'''
__VIEWSTATE: XZtxgZw+i2vNpO2FpQv/9wqAra+Fh/N6NVifTr5T34mcrXy19WGHotAZfA+sUxwEXxpOpcynQtE6rPp4f0qhY7x76qxDCVrhCgK0CSzz34zn+HMYvvnBGordUKCyGL0aXYxYnK1WQ+MpMtO1372z7rlZZFc=
__VIEWSTATEGENERATOR: C93BE1AE
from: http://so.gushiwen.cn/user/collect.aspx
email: 18394604239
pwd: c299792458
code: spta
denglu: 登录
'''

import requests
from bs4 import BeautifulSoup


url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'
}
# 获取页面源码（返回HTML页面）
response = requests.get(url=url, headers=headers)
content = response.text

# 解析页面（xpath或bs4）获取__VIEWSTATE，__VIEWSTATEGENERATOR的值
soup = BeautifulSoup(content, 'lxml')
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewstatgenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

# 解析验证码
# 获取验证码URL
# https://so.gushiwen.cn/ //img[@id="imgCode"]/@src
code = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'https://so.gushiwen.cn/' + code
# 下载内容并识别内容 不能使用urlretrieve下载，会提交两次请求，验证码就变了
# session 让访问内容是同一个对象
session = requests.session()
# 验证码的URL的内容
response_code = session.get(code_url)
# 图片下载要用二进制
content_code = response_code.content
# wb将二进制写入文件
with open('code.jpg', 'wb') as fp:
    fp.write(content_code)
code = input('input code:')

# 登录
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data_post = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstatgenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '18394604239',
    'pwd': 'c299792458',
    'code': code,
    'denglu': '登录',
}
# session 请求
response_post = session.post(url=url_post, data=data_post, headers=headers)
content_post = response_post.text

with open('gushiwen.html', 'w', encoding='utf-8') as f:
    f.write(content_post)
```

识别验证码：

> 超级鹰平台：http://www.chaojiying.com/user/
>
> 下载python对应压缩包，调用即可

## <span style="color: orange;">request库的四种异常</span>

- `ConnectionError`：网络问题
    - DNS查询失败
    - 拒接连接
- `HTTPError`：HTTP请求返回不成功的状态码
- `Timeout`：请求超时
- `TooManyRediects`：请求超过最大的重定向次数

# <span style="color: cornflowerblue;">解 析</span>

### <span style="color: burlywood;">解析选取</span>

- HTML页面：xpath、bs4、正则表达式
- json数据：json

## <span style="color: orange;">Xpath</span>

> xml path language，<span style="color: red;">lxml解析器</span>
>
> 缺点：性能差，会随着页面布局的改变而改变
>
> <span style="color: red;">适合做短期少量爬取</span>

### <span style="color: burlywood;">基本语法</span>

```python
# 路径查询
// 子孙结点
/ 子节点
# 谓词查询
//div[@id]
//div[@id='maincontent']
# 属性查询
//@clasee
# 模糊查询
//div[contains(@id, 'he')]
//div[starts-with(@id, 'he')]
# 内容查询
//div/h1/text()
# 逻辑运算
//div[@id='head' and @class='s_down']
//title | //price
```

### <span style="color: burlywood;">解析本地文件</span>

> etree.parse

```python
from lxml import etree


# xpath解析本地文件
tree = etree.parse('test.html')
# tree.xpath('xpath路径')
# 查找ul下面的li
li_list = tree.xpath('//body/ul/li/text()')
# 查找所有有id属性的li标签
li_list = tree.xpath('//ul/li[@id]')
# 找到id为li的里标签
li_list = tree.xpath('//ul/li[@id="li"]')
# 查找id=l1的li标签的 class的属性值
li = tree.xpath('//ul/li[@id="l1"]/@class')
# 找到id中包含'l'的标签
li_list = tree.xpath('//ul/li[contains(@id, "l")]')
# 找到id中以'c'开头的标签
li_list = tree.xpath('//ul/li[starts-with(@id, "c")]')
# 查询id为li和class为c1的标签
li_list = tree.xpath('//ul/li[@id="l1" and @class="c1"]')
# 查询id为l1或class为c1的标签
li_list = tree.xpath('//ul/li[@id="l1" | @id="l2"]')

print(li_list)
```

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

    <head>
        <title>测试</title>
        <meta http-equiv="content-type" content="text/html;charset=utf-8" />
        <meta name="generator" content="Geany 1.38" />
    </head>

    <body>
        <ul>
            <li id='l1' class='c1'>北京</li>
            <li id='l2'>上海</li>
            <li id='c3'>广州</li>
            <li id='c4'>深圳</li>
        </ul>
    </body>

</html>

```

### <span style="color: burlywood;">解析服务器响应的数据</span>

> etree.HTML()
>
> xpath返回值为列表

```python
# 爬取站长素材的图片
from urllib.request import Request, urlopen, urlretrieve
from lxml import etree


def create_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = f'https://sc.chinaz.com/tupian/qinglvtupian_{page}.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64'
    }
    request = Request(url, headers=headers)
    return request
    

def get_content(request):
    response = urlopen(request)
    content = response.read().decode('utf-8')
    return content
    
    
def download_img(content):
    tree = etree.HTML(content)
    img_urls = tree.xpath('//img[@class="lazy"]/@data-original')
    name_list = tree.xpath('//img[@class="lazy"]/@alt')
    for i in range(len(img_urls)):
        img_url =  img_urls[i]
        name = name_list[i]
        url = f'https:{img_url}'
        filename = f'./img/{name}.jpg'
        urlretrieve(url, filename)
    

def main():
    start_page = int(input('input start page:'))
    end_page = int(input('input end page:'))
    for page in range(start_page, end_page+1):
        request = create_request(page)
        content = get_content(request)
        download_img(content)
        

if __name__ == '__main__':
    main()
```

## <span style="color: orange;">jsonPath</span>

> 使用于解析json数据
>
> 只能解析本地文件

```python
# 基本语法
from jsonpath import jsonpath
import json


obj = json.load(open('test.json', 'r'))
# 找book的所有作者
author = jsonpath(obj, '$.store.book[*].author')
# 查询store所有的作者
author_list = jsonpath(obj, '$..author')
# store中所有元素
tag_list = jsonpath(obj, '$.store.*')
# store中所有的价格
price_list = jsonpath(obj, '$.store..price')
# 第三本书
book = jsonpath(obj, '$..book[2]')
# 最后一本书
book = jsonpath(obj, '$..book[(@.length-1)]')
# 前两本书book方括号里不能有空格 book[0, 1]
book = jsonpath(obj, '$..book[0,1]')
book = jsonpath(obj, '$..book[:2]')
# 过滤出所有含isbn的书,条件过滤?()
book_list = jsonpath(obj, '$..book[?(@.isbn)]')
# price超过10的书
book_list = jsonpath(obj, '$..book[?(@.price>10)]')

print(book_list)
```

```python
# 爬淘票票的所有城市
from urllib.request import Request, urlopen
import json
from jsonpath import jsonpath


url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1683080264428_112&jsoncallback=jsonp113&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers = {
    # 本例无需cookie
    #'cookie':' cna=cSWwG2AScmYCASeQ03f0nBxL; miid=1114709535307545168; t=f3ee78be96003fb3bc906ba9b51f1f3e; cookie2=19eed9d0a9b9becba21c7299e76c8f58; v=0; _tb_token_=e9e7e8eb3eb9f; xlly_s=1; _m_h5_tk=4dd5e4bb570b2d995f7a24e77b1dcf5c_1683085045051; _m_h5_tk_enc=f9ea6acb7607c597e66ffba2aa1f2a94; _samesite_flag_=true; sgcookie=E100e%2FmdD3koOSCQUPWVPfz%2BJ4Fqvq%2FISix66nvJPhXJlIFheAORQPkm7LHiY7pxw%2FpHpBGYVdQ3c33riIrHzJmvG4Zjk0XY0snvJvZgAKXv01klUG8TSnFZy6DBuEp%2BWShP; unb=2662676332; uc3=lg2=UtASsssmOIJ0bQ%3D%3D&vt3=F8dCsfPk%2FFF%2B%2BxWwFP8%3D&id2=UU6nQ%2FuGtpJ%2BPA%3D%3D&nk2=tMvNOuz%2B5ga1lg%3D%3D; csg=6ace3dfe; lgc=%5Cu81EA%5Cu8840%5Cu6218%5Cu4E2D%5Cu534E; cancelledSubSites=empty; cookie17=UU6nQ%2FuGtpJ%2BPA%3D%3D; dnk=%5Cu81EA%5Cu8840%5Cu6218%5Cu4E2D%5Cu534E; skt=83f8c52ad30d2554; existShop=MTY4MzA3OTAyNg%3D%3D; uc4=nk4=0%40ti1CU368eVwHKeZ%2Fg4ewjU04YR%2B5&id4=0%40U2xqJxDU8MlsM2pRllNXyoOoryCr; tracknick=%5Cu81EA%5Cu8840%5Cu6218%5Cu4E2D%5Cu534E; _cc_=U%2BGCWk%2F7og%3D%3D; _l_g_=Ug%3D%3D; sg=%E5%8D%8E21; _nk_=%5Cu81EA%5Cu8840%5Cu6218%5Cu4E2D%5Cu534E; cookie1=AVS2QB4rI5zJHDGbz01JJJ2QnQkr03ByfzGUvE6UHzY%3D; uc1=pas=0&existShop=false&cookie14=Uoe8idPMidS4HA%3D%3D&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie21=W5iHLLyFeYZ1WM9hVnmS&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D; tfstk=cGrPBAtpjgIPrSed6mmUgsBpQb0RZ8nnXIkIr6CT2r1cKmglivRKnmOnuV92t4f..; l=fB_t9KhPNa5G4ilfBOfanurza77tvIRYouPzaNbMi9fPOO5H5KmFW1wfFQTMCnGVFs3WR3-bnsADBeYBqC2sjqj4axom4xMmnmOk-Wf..; isg=BPT0IH2YLHbOqbhML4CWUowbxbJmzRi3xkPcS45Vt38C-ZRDtt0uR-m3eTEhB1AP',
    'referer': 'https://dianying.taobao.com/',
    'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68',
}

request = Request(url, headers=headers)
response = urlopen(request)
content = response.read().decode('utf-8')

content = content.split('(')[1].split(')')[0]

with open('test.json', 'w', encoding='utf-8') as f:
    f.write(content)

with open('test.json', 'r', encoding='utf-8') as f:
    obj = json.load(f)

city_list = jsonpath(obj, '$..regionName')
print(city_list)
```

## <span style="color: orange;">jsonPath语法与xPath语法对比</span>

| **XPath** | **JSONPath**       | **Description**                                              |
| --------- | ------------------ | ------------------------------------------------------------ |
| /         | $                  | 表示根元素                                                   |
| .         | @                  | 当前元素                                                     |
| /         | . or \[\]          | 子元素                                                       |
| …         | n/a                | 父元素                                                       |
| //        | …                  | 递归下降，JSONPath是从E4X借鉴的。                            |
| *         | *                  | 通配符，表示所有的元素                                       |
| @         | n/a                | 属性访问字符                                                 |
| \[\]      | \[\]               | 子元素操作符                                                 |
| \|        | \[,\]              | 连接操作符在XPath 结果合并其它结点集合。JSONP允许name或者数组索引。 |
| n/a       | `[start:end:step]` | 数组分割操作从ES4借鉴。                                      |
| \[\]      | ?()                | 应用过滤表示式                                               |
| n/a       | ()                 | 脚本表达式，使用在脚本引擎下面。                             |
| ()        | n/a                | Xpath分组                                                    |

## <span style="color: orange;">BS4</span>

> 是<span style="color: red;">HTML解析器</span>
>
> 效率没lxml高，但使用方便
>
> 默认`soup`是`BeautifulSoup`对象
>
> 官方文档：https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh

### <span style="color: burlywood;">常用对象</span>

- `BeautifulSoup`对象
- `Tag`对象
- `NavigableString`对象：用来表示标签里的文字
- `Comment`对象：用来查找HTML文档的注释标签

```python
from bs4 import BeautifulSoup


# (服务器文件)创建对象
soup = BeautifulSoup(response.read().decode('utf-8'), 'lxml')
# (本地文件)默认打开的文件格式是gbk
soup = BeautifulSoup(open('test.html', encoding='utf-8'), 'lxml')

# 根据标签名查找节点，找到第一个符合条件的数据
print(soup.ul)
# 获取标签的属性和属性值
print(soup.ul.li.attrs)
```

### <span style="color: burlywood;">soup.find()</span>

> `find_all()` 方法将返回文档中符合条件的所有tag
>
> `limit=1`时，两者的唯一的区别是 `find_all()` 方法的返回结果是值包含一个元素的列表,而 `find()` 方法直接返回结果.

```python
from bs4 import BeautifulSoup


# (服务器文件)创建对象
# soup = BeautifulSoup(response.read().decode('utf-8'), 'lxml')
# (本地文件)默认打开的文件格式是gbk
soup = BeautifulSoup(open('test.html', encoding='utf-8'), 'lxml')

# 返回第一个符合条件的数据
print(soup.find('ul'))
# 通过标签找标签对象
print(soup.find('li', id='c3'))
# 根据class的值找到标签对象，class需要加下划线
print(soup.find('li', class_='c1'))
```

### <span style="color: burlywood;">soup.find_all()</span>

> 通过标签的不同属性过滤HTML页面，结果返回为列表

find_all(name, attributes, recursive, text, **keywords)

- `name`: 检索标签名称
- `attributes`: 对标签属性值的检索字符串，可标注属性检索
- `recursive`: 布尔变量，对子孙全部检索，默认为true
- `text`: 标签结点中文本
- `**keywords`: 可选参数

```python
from bs4 import BeautifulSoup


# (服务器文件)创建对象
# soup = BeautifulSoup(response.read().decode('utf-8'), 'lxml')
# (本地文件)默认打开的文件格式是gbk
soup = BeautifulSoup(open('test.html', encoding='utf-8'), 'lxml')

# 返回所有符合条件的数据 列表
print(soup.find_all('ul'))
# 通过标签找标签对象，向获取多个标签的数据，需要把标签放在列表中
print(soup.find_all(['li', 'id']))
# 返回前两个数据
print(soup.find_all('li', limit=2))
```

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

    <div>
        <head>
            <title>测试</title>
            <meta http-equiv="content-type" content="text/html;charset=utf-8" />
            <meta name="generator" content="Geany 1.38" />
        </head>

        <body>
            <ul>
                <li id='l1' class='c1'>北京</li>
                <li id='l2'>上海</li>
                <li id='c3'>广州</li>
                <li id='c4'>深圳</li>
            </ul>

            <ul>
                <li>西峰</li>
                <li>西安</li>
                <li>华池</li>
            </ul>

        </body>
    </div>
    
    <div id="d1">
        <span>嘻嘻嘻</span>
    </div>
    <p id="d2">哈哈哈</p>
</html>

```

### <span style="color: burlywood;">soup.select()</span>

> 使用CSS选择器语法找tag

#### 选择器

> 选择标签对象

```python
from bs4 import BeautifulSoup


# (服务器文件)创建对象
# soup = BeautifulSoup(response.read().decode('utf-8'), 'lxml')
# (本地文件)默认打开的文件格式是gbk
soup = BeautifulSoup(open('test.html', encoding='utf-8'), 'lxml')

# 返回所有符合条件的数据 列表
print(soup.select('ul'))
# 通过点代表class（类选择器）
print(soup.select('.c1'))
# 通过井号找id
print(soup.select('#l2'))

# 属性选择器 - 通过属性寻找对应标签对象
# 查找到li中有id的标签
print(soup.select('li[id]'))
# 查找id为l2的标签
print(soup.select('li[id="l2"]'))

# 层级选择器
# 空格 - 后代选择器
# div下的li
print(soup.select('div li'))
# 大于号 - 子代选择器
print(soup.select('div>ul>li'))
# 逗号 - 列表标签
print(soup.select('li,id'))
```

#### 结点信息

> 选择标签中的内容

```python
from bs4 import BeautifulSoup


# (服务器文件)创建对象
# soup = BeautifulSoup(response.read().decode('utf-8'), 'lxml')
# (本地文件)默认打开的文件格式是gbk
soup = BeautifulSoup(open('test.html', encoding='utf-8'), 'lxml')

obj = soup.select('#d1')[0]
# 如果标签对象中只有内容，string和get_text()一样
# 如果标签对象中除了内容还有标签，string不能获取到内容
print(obj.string)
print(obj.get_text())

# 节点的属性 
# name是标签的名字
obj = soup.select('#d2')[0]
print(obj.name)
# 将属性值作为字典返回
print(obj.attrs)

# 获取节点的属性
obj = soup.select('li[id="l1"]')[0]
print(obj.attrs.get('class'))
print(obj.get('class'))
print(obj['class'])
```

```python
# 解析星巴克的商品名字
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


url = 'https://www.starbucks.com.cn/menu/'
response = urlopen(url)
content = response.read().decode('utf-8')
soup = BeautifulSoup(content, 'lxml')
# xpath语法先确定对象
# //ul[@class="grid padded-3 product"]//strong/text()
name_list = soup.select('ul[class="grid padded-3 product"] strong')
for name in name_list:
    print(name.get_text())
```

### <span style="color: burlywood;">例 | BS4爬取微信读书的一本书目录</span>

```python
# 爬取‘微信读书’的一本书目录
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


def create_request():
    url = 'https://weread.qq.com/web/reader/6c532640716e83076c508efk71a32680332f71ad16addf2?'
    headers = {	
        
        'cookie':'pgv_pvid=8176361922; RK=x81MxGjlxC; ptcz=d164f7a8dff40507a5773cd39fcf2c9fce42bfeffc175e82b9cc9f7485a26512; ptui_loginuin=3530894087; wr_avatar=; wr_gid=242693918; wr_fp=4029444045; wr_vid=434438692; wr_skey=_G_QWIpc; wr_pf=0; wr_rt=web%40V3MQ8vDM0DUKCxJ3BED_AL; wr_localvid=48332990819e50224483c84; wr_name=%E5%BE%AE%E4%BF%A1%E7%94%A8%E6%88%B7; wr_gender=0',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
    }
    request = Request(url, headers=headers)
    return request


def get_content(request):
    response = urlopen(request)
    content = response.read().decode('utf-8')
    return content
    

def download(content):
    soup = BeautifulSoup(content, 'lxml')
    # //ul[@class="readerCatalog_list"]//span/text()
    catalogue_list = soup.select('ul[class="readerCatalog_list"] span')
    for catalogue in catalogue_list:
        with open('book.txt', 'a') as f:
            f.write(catalogue.get_text() + '\n')
    

def main():
    request = create_request()
    content = get_content(request)
    download(content)
    
    
if __name__ == '__main__':
    main()
```

### <span style="color: burlywood;">例 | 爬取酷狗音乐Top500的歌单信息并保存</span>

```python
import requests
from bs4 import BeautifulSoup
import time
import json


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}


def get_info(url):
    '''根据网址获取信息的函数'''
    wb_data = requests.get(url, headers=headers)
    # 使用HTML解析器
    soup = BeautifulSoup(wb_data.text, 'html.parser')
    # 尽量不使用完整的selector
    ranks = soup.select('span.pc_temp_num')
    titles = soup.select('div.pc_temp_songlist > ul > li > a')
    times = soup.select('span.pc_temp_tips_r > span')
    for rank, title, time in zip(ranks, titles, times):
        data = {
            'rank': rank.get_text().strip(),
            'singer': title.get_text().split('-')[0].strip(),
            'song': title.get_text().split('-')[1].strip(),
            'time': time.get_text().strip(),
        }
        datas.append(data)

        
def save_file():
    '''把数据保存为json文件和格式化的text文件'''
    
    # 文件名
    json_filename = '酷狗Top500歌单信息.json'
    txt_filename = '酷狗Top500歌单信息.txt'
    
    for data in datas:
        with open(json_filename, 'a', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        msg = f"第{data['rank']}名，歌名《{data['song']}》，由{data['singer']}演唱，时长：{data['time']}\n"
        with open(txt_filename, 'a', encoding='utf-8') as f:
            f.write(msg)
    print('写入成功')

    
def main():
    # data保存为全局
    global datas
    datas = []
    urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format\
    (str(i)) for i in range(1, 24)]
    for url in urls:
        get_info(url)
    save_file()

    
if __name__ == '__main__':
    main()
```

## <span style="color: orange;">导航树</span>

### <span style="color: burlywood;">子标签</span>

- `children()`: 父标签的下一级
- `descendant()`: 父标签下的所有

### <span style="color: burlywood;">兄弟标签</span>

- `next_siblings()`: 当前标签其后的同级标签
- `previous_siblings()`：当前标签前的同级标签

### <span style="color: burlywood;">父标签</span>

- `parent()`: 当前标签的上一层
- `parents()`: 当前标签的上次所有

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
    
    
def main():
    html = urlopen('https://pythonscraping.com/pages/page3.html')
    soup = BeautifulSoup(html, 'lxml')
    # 让标签的选择更加具体：
    for sibling in soup.find('table', {'id':'giftList'}).next_siblings:
        print(sibling)

if __name__ == '__main__':
    main()
```

# <span style="color: cornflowerblue;">正则表达式</span>

## <span style="color: orange;">字符及含义</span>

### <span style="color: burlywood;">一般字符</span>

| 字符    | 含义                             |
| ------- | -------------------------------- |
| `.`     | 匹配任意单个字符（不包括换行符） |
| `\`     | 转义字符                         |
| `[...]` | 字符集（任选一个）               |

### <span style="color: burlywood;">预定义字符</span>

| 预定义字符集 | 含义                                       |
| ------------ | ------------------------------------------ |
| `\d`         | 数字字符，等价于\[0,9\]                    |
| `\D`         | 非数字字符，等价于<sup>[\[1\]](#fn1)</sup> |
| `\s`         | 空白字符，等价于\[\\n\\t\\f\\r\\v\]        |
| `\S`         | 非空白字符                                 |
| `\w`         | 包括下划线的任意单词字符\[A-Za-z0-9\]      |
| `\W`         | 包括任何非单词字符                         |

### <span style="color: burlywood;">数量词</span>

| 数量词  | 含义                    |
| ------- | ----------------------- |
| `*`     | 匹配前一个字符0或无限次 |
| `+`     | 匹配前一个字符1或无限次 |
| `?`     | 匹配前一个字符0或1次    |
| `{m}`   | 匹配前一个字符m次       |
| `{m,n}` | 匹配前一个字符\[m,n\]次 |

### <span style="color: burlywood;">边界匹配</span>

> 爬虫不常用

| 边界匹配 | 含义             |
| -------- | ---------------- |
| `^`      | 匹配字符串开头   |
| `$`      | 匹配字符串结尾   |
| `\A`     | 仅匹配字符串开头 |
| `\Z`     | 仅匹配字符串结尾 |

### <span style="color: burlywood;">爬虫常用</span>

`?` 字符紧跟在任何一个其他限制符`（*,+,?，{n}，{n,}，{n,m}）`后面时，匹配模式是**非贪婪**的。

| 符号                                | 含义                                            | 例子              | 匹配结果               |
| ----------------------------------- | ----------------------------------------------- | ----------------- | ---------------------- |
| *                                   | 匹配前面的字符、子表达式或括号里的字符0次或多次 | a*b               | aaab,ab,b              |
| +                                   | 匹配前面的字符、子表达式或括号里的字符至少1次   | a+b+              | abbb,aaab              |
| \[\]                                | 任选一个                                        | \[A-Z\]*          | 仅由大写字母组成       |
| ()                                  | 表达式组编（优先匹配）                          | (a\*b)\*          | abaab,aaabaab,baaab    |
| {m, n}                              | 匹配前面的字符、子表达式或括号里的字符m-n次     | a{2,3}            | aa,aaa                 |
| \[^\]                               | 匹配任意一个不在中括号里的字符                  | \[^A-Z\]*         | 不包括大写字母         |
| \|                                  | 匹配一个由竖线分割的子表达式                    | b(a\|i\|e)d       | bad,bid,bed            |
| .                                   | 匹配任意单个字符                                | b.d               | bid,bad,b%d            |
| ^                                   | 字符串开始位置的字符或子表达式                  | ^d                | deck,d                 |
| \                                   | 转义字符                                        | \\\               | \                      |
| $                                   | 从字符串的末端匹配                              | \[A-Z\]*\[a-z\]*$ | Abc, Bob               |
| <span style="color: red;">?!</span> | 不包含                                          | ^((?!\[A-Z\]).)*$ | 从头到尾不包括大写字母 |

## <span style="color: orange;">re模块</span>

> re模块使python拥有全部的正则表达式功能

### <span style="color: burlywood;">re.search(pattern, string, flags=0)</span>

> - pattern: 匹配的正则表达式
> - string: 待匹配的字符串
> - flags: 控制匹配方式（是否区分大小写，多行匹配等）
>
> 提取第一个符合规律的内容，并返回一个表达式对象

```python
import re


a = 'one1two2three3'
infos = re.search('\d',a)
# group把正则表达式对象转为字符
# 若没有匹配到字符串，再使用group会出现AttributeError
print(infos.group()) # 1
```

### <span style="color: burlywood;">re.sub(pattern, repl, string, count=0, flags=0)</span>

> - repl: 替换的字符串
> - count: 替换的最大次数，默认为0，表示替换所有
>
> 替换字符串中的匹配项

```python
import re


phone = '123-456-789'
new_phone = re.sub('\D', '', phone,)
print(new_phone) # 123456789
```

### <span style="color: burlywood;">re.findall(pattern, string, flags=0)</span>

> 匹配所有符合规律的内容，以列表形式返回

```python
import re


a = 'one1two2three3'
res = re.findall('\d+', a)
print(res) # ['1', '2', '3']
```

### <span style="color: burlywood;">re模块修饰符</span>

> 通过可选标志修饰符控制字符的匹配模式

| 修饰符 | 描述                                                         |
| ------ | ------------------------------------------------------------ |
| `re.I` | 大小写不敏感                                                 |
| `re.L` | 做本地化识别匹配                                             |
| `re.M` | 多行匹配，影响`^`和`$`                                       |
| `re.S` | 匹配包括换行在内的所有字符                                   |
| `re.U` | 根据字符集Unicode【国际标准字符集】解析字符。这个标志影响`\w`，`\W`，`\b`，`\B` |
| `re.X` | 格式？                                                       |

```python
# 例
import re


a = '''<div>指数
</div>'''
word = re.findall('<div>(.*?)</div>', a, re.S) # re.S用于跨行
print(word[0].strip()) # 指数
```

### <span style="color: burlywood;">例 | 正则表达式配合BS4</span>

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
    
    
def main():
    html = urlopen('https://pythonscraping.com/pages/page3.html')
    soup = BeautifulSoup(html, 'lxml')
    # re.compile: 将正则表达式编译为一个pattern对象
    images = soup.find_all('img', {'src':re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
    for image in images:
        # 获取标签属性的值
        print(image['src'])
        # 获取image的所有属性
        print(image.attrs)


if __name__ == '__main__':
    main()
```

# <span style="color: cornflowerblue;">Lxml库与Xpath语法</span>

> 高效解析HTML和XML文档

```python
# 用Xpath解析HTML文件
import requests
from lxml import etree


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/\
    537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
}

res = requests.get('https://movie.douban.com/top250', headers=headers)
html = etree.HTML(res.text)
result = etree.tostring(html)
print(result)
```

## <span style="color: orange;">Xpath语法</span>

> 在XML文档中查找信息的语言

### <span style="color: burlywood;">节点关系</span>

- 父节点
- 子节点
- 同胞节点
- 先辈节点
- 后代节点

### <span style="color: burlywood;">节点选择</span>

| 表达式     | 描述                           | 示例                  | 示例说明                                      |
| ---------- | ------------------------------ | --------------------- | --------------------------------------------- |
| `nodename` | 选取此节点的所有子节点         | `user_database`       | 选取元素`database`的所有子节点                |
| `/`        | 从根节点选取                   | `/user_database`      | 选取根元素`user_database`                     |
|            |                                | `user_database/user`  | 选取属于`user_database`子元素的所有`user`元素 |
| `//`       | 从匹配的当前结点选择文档的结点 | `//user`              | 选取所有的`user`子元素                        |
|            |                                | `user_database//user` | 选择属于`user_database`的后代的所有元素       |
| `.`        | 选取当前结点                   |                       |                                               |
| `..`       | 选取当前结点的父节点           |                       |                                               |
| `@`        | 选取属性值                     | `//@attribute`        | 选取名为`attribute`的所有属性值               |

路径表达式可也搭配谓词、通配符

谓词被嵌在方括号里，如：`//li[@attribute]`，选取拥有名为`attribute`属性的`li`元素

记录断点：

- 爬豆瓣的TOP250，存入csv文件
- 先学xpath
- 再调试test代码

## <span style="color: orange;">lxml</span>

> 官方文档：https://lxml.de/index.html

# <span style="color: cornflowerblue;">Selenium</span>

> 用于web应用程序测试的工具，selenium测试直接运行在浏览器中，就像真正的用户在操作一样

## <span style="color: orange;">有界面浏览器的使用</span>

> selenium的使用

### <span style="color: burlywood;">配置</span>

```python
# 下载浏览器的驱动
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ # edge的驱动
# 安装selenium
pip install selenium -i https://douban.com/simple
```

### <span style="color: burlywood;">基本使用</span>

```python
from urllib.request import Request, urlopen
from selenium import webdriver


# 创建浏览器操作对象
path = 'msedgedriver.exe'
browser = webdriver.Edge(path)

# 访问网站
url = 'https://www.jd.com/'
browser.get(url)
# 获取网页源码
content = browser.page_source
print(content)
```

### <span style="color: burlywood;">元素定位</span>

```python
from selenium import webdriver
from selenium.webdriver.common.by import By


# 创建浏览器操作对象
path = 'msedgedriver.exe'
browser = webdriver.Edge(path)

url = 'https://cn.bing.com/'
browser.get(url)

# 元素定位
# 根据id找到对象【常用】
button = browser.find_element(By.ID, 'sb_form_go')
# 根据name属性值查找
button = browser.find_element(By.NAME, 'q')
# 根据类名获取对象
button = browser.find_element(By.CLASS_NAME, 'scope_cont')
# 根据标签名查找对象(蓝源码中蓝色的)
button = browser.find_element(By.TAG_NAME, 'img')
# 根据xpath语句获取对象【常用】
button = browser.find_element(By.XPATH, '//input[@id="sb_form_q"]')
# 根据css选择器获取对象【常用】
button = browser.find_element(By.CSS_SELECTOR, 'input[id="sb_form_q"]')
# 获取链接文本的对象
button = browser.find_element(By.PARTIAL_LINK_TEXT, '动物')
print(button)
```

### <span style="color: burlywood;">元素信息及交互</span>

```python
# 元素信息
from selenium import webdriver
from selenium.webdriver.common.by import By


# 创建浏览器操作对象
path = 'msedgedriver.exe'
browser = webdriver.Edge(path)

url = 'http://www.baidu.com'
browser.get(url)
# 获取标签的属性值(<tag='value'>)
input = browser.find_element(By.ID, 'su')
print(input.get_attribute('class'))
# 获取标签名（<tag>）
print(input.tag_name)
# 获取元素文件(<>text<>)
a = browser.find_element(By.LINK_TEXT, '新闻')
print(a.text)
```

```python
# 运行浏览器，执行操作
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 创建浏览器对象
path = 'msedgedriver.exe'
browser = webdriver.Edge(path)

url = 'https://www.baidu.com'
browser.get(url)
# 睡眠两秒
time.sleep(2)
# 获取文本框的对象
input = browser.find_element(By.ID, 'kw')
# 在文本框中输入‘毛不易’
input.send_keys('毛不易')

time.sleep(2)

# 获取百度一下的按钮
find_button = browser.find_element(By.ID, 'su')
# 点击按钮
find_button.click()

time.sleep(2)

# 划到底部
js_buttom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_buttom)
time.sleep(2)
# 获取下一页
next_button = browser.find_element(By.CLASS_NAME, 'n')
next_button.click()

time.sleep(2)

# 回退
browser.back()
time.sleep(2)
# 前进
browser.forward()

time.sleep(3)
# 退出浏览器
browser.quit()
```

## <span style="color: orange;">无界面浏览器</span>

### <span style="color: burlywood;">phantomjs</span>

> 已停更

```python
# 和selenium操作一致
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


path = 'phantomjs.exe'
# 由于selenium版本过高，因此没有PhantomJS方法（Phantomjs已停更）
browser = webdriver.PhantomJS(path)

url = 'https://www.baidu.com'
browser.get(url)
# 保存快照
broswer.save_screenshot('baidu.png')

input = browser.find_element(By.ID, 'kw')
input.send_keys('李白')
time.sleep(2)
browser.save_screenshot('libai.png')
```

### <span style="color: burlywood;">chrome handless</span>

```python
# 和selenium操作一致
```

# <span style="color: cornflowerblue;">scrapy采集</span>

> 一个为了爬取网页数据，提取结构性数据而编写的应用框架。

## <span style="color: orange;">scrapy工作原理</span>

下载pip

```python
# pip install scrapy
```

scrapy架构

![6d7789a55ef6206ee21b8d290abc4e84.png](resources/985521de2dbe49a681bd1e13b4ff7a33.png)

6d7789a55ef6206ee21b8d290abc4e84.png

6d7789a55ef6206ee21b8d290abc4e84.png

![scrapy运行过程.png](resources/b63a0ef81ab645daa7d40dc9cc97bf2a.png)

scrapy运行过程.png

1.  引擎向spiders要URL
2.  引擎将要爬取的URL给调度器
3.  调度器生成请求对象，将其放入指定队列
4.  队列出队一个请求
5.  引擎将请求交给下载器处理
6.  下载器发送请求获取互联网数据
7.  下载器将数据返回给引擎
8.  引擎将数据再次给到spiders
9.  spiders通过xpath解析该数据，获得数据或URL
10.  spiders将数据或URL给引擎
11.  引擎判断来自spders的内容
     - 是URL：交给调度器处理
     - 是数据：交给管道处理

## <span style="color: orange;">基本使用</span>

### <span style="color: burlywood;">项目的创建及运行</span>

```python
# 1.创建爬虫的项目
scrapy startproject project_name
'''
project_name: 不能以数字开头，不能有中文
'''
```

```python
# 项目组成
'''
文件结构
project_name
    |- scrapy.cfg
    |- project_name
        |- __init__.py    
        |- items.py    定义数据结构的地方（爬取的数据有哪些），是一个继承自scrapy.Item的类
        |- middlewares.py    中间件，代理
        |- piplines.py    管道文件，里面只有一个类，用于实现下载数据的后续处理（值越小，优先级越高 1-1000）
        |- settings.py    配置文件 比如：是否遵循robots协议，UA定义等
        |- spiders
            |- __init__.py    存储爬虫文件
            |- 自定义的爬虫文件.py    由我们自己创建，实现爬虫核心功能的文件
'''
```

```python
# 2.创建py文件
scrapy genspider 爬虫的名字 爬取网页 # scrapy genspider baidu http://www.baidu.com
```

```python
# 3.运行爬虫代码
scrapy crawl 爬虫的名字 # scrapy crawl baidu
```

每次修改完代码都要保存，再运行

```python
# response的属性和方法
response.text # 获取响应的字符
response.body # 获取响应的二进制数据
response.xpath('') # 可用xpath方法解析response中的内容
response.extract() # 提取selector对象的data属性值
response.extract_first() # 提取selector列表的第一个数据
```

## <span style="color: orange;">scrapy shell</span>

> 作用：大项目调试

进入到scrapy shell的终端，直接在window的终端输入scrapy shell 域名

`ipython`：高亮、自动补全

进入方式：`scrapy shell www.baidu.com`

## <font color='orange'>CrawlSpider</font>

>   可以定义规则，解析HTML的内容的时候根据规则提取指定链接，适用于跳转爬取

### <font color='BurlyWood'>基本使用</font>

```python
# 创建爬虫类
scrapy genspider -t crawl read www.dushu.com
# 链接提取器
scrapy.linkextractors.LinkExtractor{
    allow = () # 提取符合正则的链接
    deny = () # 不用正则表达式
    allow_domains() # 不用允许的域名
    deny_domains() # 不用不允许的域名
    restrict_xpath = () # 提取符合xpath的链接
    restrict_css = () # css选择器   
}
# 例-使用
links1 = LinkEctractor(allow=r'list_23_\d\.html')
links2 = LinkExtractor(restrict_xpath=r'//div[@class="x"]')
links3 = LinkExtractor(restrict_css='.x')
# 提取链接
link.extract_links(response)
```

## <font color='orange'>日志信息</font>

### <font color='BurlyWood'>日志级别</font>

-   CRITICAL：严重错误
-   ERROR：一般错误
-   WARNING：警告
-   INFO：一般信息
-   DEBUG：调试信息

默认日志等级：debug。只要出现debug及以上等级，都会打印

### <font color='BurlyWood'>setting文件配置</font>

LOG_FILE：将屏幕信息全部记录在文件中，屏幕不在显示（注：文件后缀是`.log`)

LOG_LEVEL：设置日志显示等级

## <font color='orange'>post请求</font>

>   post请求依赖于参数，如果没有参数，则该请求没有意义

```python
import scrapy
import json


class PostSpider(scrapy.Spider):
	name = "post"
	allowed_domains = ["fanyi.baidu.com/sug"]
	# 使用post请求的url，start_url和parse请求均失效
	#start_urls = ["https://fanyi.baidu.com/sug"]

	#def parse(self, response):
	#	pass

	# post请求的使用
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
```
