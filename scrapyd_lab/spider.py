import scrapy


class MingYan(scrapy.Spider): #需要继承scrapy.Spider类
    name = "mingyan" #定义名字

    start_urls = [        #另一种写法，无需定义start_requests方法
            'http://lab.scrapyd.cn/page/1/',
            'http://lab.scrapyd.cn/page/2/',
        ]

    # def start_requests(self): #通过此方法爬起下面链接页面
    #     #定义爬取得链接
    #     urls=[
    #         'http://lab.scrapyd.cn/page/1/',
    #         'http://lab.scrapyd.cn/page/2/',
    #     ]
    #     for url in urls:    #爬取到的页面，提交给parse方法
    #         yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        #根据上面的链接提取分页
        page=response.url.split("/")[-2]
        #拼接文件名
        filename='mingyan-%s.html' % page
        with open(filename, 'wb')as f:   #python文件操作
            f.write(response.body)

            self.log('保存文件:%s' % filename) #打印日志
