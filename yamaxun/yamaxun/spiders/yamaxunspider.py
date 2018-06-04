from scrapy import Spider,Request
import json
import re
from urllib.parse import quote
from lxml import etree
from yamaxun.items import YamaxunItem
key ='华为'

class YamaxunSpider(Spider):
    name = 'yamaxun'


    def start_requests(self):

        for i in  range(2):
            url = 'https://www.amazon.cn/s?ie=UTF8&page={}&rh=n%3A664978051%2Ck%3A{}'.format(str(i+1),quote(key))
            yield Request(url=url, callback=self.parse_get_info,meta={'download_timeout':3})
            #yield Request(url='http://httpbin.org/get', callback=self.parse,meta={'download_timeout':5})

    def parse(self, response):
        print(response.text)
    def parse_get_info(self, response):
        selector = etree.HTML(response.text)

        infos = selector.xpath('//ul[@id="s-results-list-atf"]/li')



        for info in infos:

            item = YamaxunItem()
            ID = info.xpath('@data-asin')
            name = info.xpath('div/div[3]/div/a/@title')
            price = info.xpath('div/div[@class="a-row a-spacing-mini"]/div/a/span/text()')
            score =info.xpath('div/div[@class="a-row a-spacing-none"]/span/span/a/i/span/text()')
            comments_total=info.xpath('div/div[@class="a-row a-spacing-none"]/a/text()')#评论人数
            comment_url =info.xpath('div/div[3]/div[1]/a/@href')[0]
            yield Request(url=comment_url,callback=self.parse_get_comment, meta={'id':ID,'name':name,'price':price,'score':score,'comments_total':comments_total,'download_timeout':3})








    def parse_get_comment(self, response):

        selector = etree.HTML(response.text)
        comments = selector.xpath('//div[@id="cm-cr-dp-review-list"]/div')

        comment_total=[]



        if comments:
            for comment in comments:
                item = YamaxunItem()
                comment_user=comment.xpath('div/div/a/div[2]/span/text()')
                comment_time=comment.xpath('div/span/text()')
                comment_data=comment.xpath('div/div[4]/span/div/div/text()')
                comment_ = {
                    'comment_user':comment_user,
                    'comment_time':comment_time,
                    'comment_data':comment_data


                }
                comment_total.append(comment_)

            item['comment_data']=comment_total
            item['ID']=response.meta['id']
            item['name']=response.meta['name']
            item['price']=response.meta['price']
            item['score']=response.meta['score']
            item['comments_total']=response.meta['comments_total']

            yield item









