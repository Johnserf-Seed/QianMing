# -*- coding:utf-8 -*- 
#Time: 2020/10/06/17:10
#Author: JohnserfSeed
#GitHub: https://github.com/Johnserf-Seed

from lxml import etree
import requests

class qm:

    #资源地址
    url = 'http://www.kachayv.cn/'

    #UA字典
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Host': 'www.kachayv.cn',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Connection': 'keep-alive',
            'Accept-Encoding': 'gzip,deflate,br',
            'Accept-Language': 'zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7'
        }

    def __init__(self,qname):
        self.down_img(qname)

    #图片下载
    def down_img(self,qname):
        data = {
            'word': qname,
            'fonts': '16.ttf',
            'sizes': '60',
            'fontcolor': '#000000',
            'colors': '#ffffff'
        }
        try:
            r = requests.post(self.url,headers=self.headers,data=data)
            res = etree.HTML(r.text)
            img_url=res.xpath('//img[@id="showImg"]/@src')
            if(img_url==[]):
                print("错误")
        except:
            pass
        else:
            for img in img_url:
                try:
                    print("正在生成...")
                    #print(self.url+img)
                    r = requests.get(self.url+img)
                    #img,'.jpg'
                    with open(qname+ '.png', 'wb') as code:
                        code.write(r.content)
                except:
                    input(print("生成出错!"))
                    exit(0)
            input(print('生成完成!!'))
            exit(0)
        return

if __name__ == "__main__":
    qname=input("输入姓名:")
    qm(qname)