import requests
from lxml import etree
import time
from urllib.request import urlretrieve
import os

url = 'http://www.netbian.com/1920x1080/index_2.htm'
head = {
    'User-Anent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
if not os.path.exists("www"):
    os.mkdir('www')

class Ison(object):

    def not_in(self):
        for i in range(2,20):
            r = requests.get(url,headers=head)
            r.encoding = 'gb2312'
            html = etree.HTML(r.text)
            self.xpath_data(html)


    def xpath_data(self,html):
        r_list = html.xpath('//*[@id="main"]/div[2]/ul/li/a')

        for i in r_list:
            pic_u = i.xpath('.//@src')[0]
            name_1 = i.xpath('.//b/text()')[0].strip( )
            print('正在下载图片_%s' % name_1)
            urlretrieve(pic_u, 'wwh/%s.jpg' % name_1)
            time.sleep(1)

ison = Ison()
ison.not_in()
