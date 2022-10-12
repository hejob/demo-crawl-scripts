from urllib.request import Request, urlopen
from lxml import etree
import io
import gzip
from bs4 import BeautifulSoup

url =  "https://www.bilibili.com/video/BV1c4411e77t/"

req = Request(url)
req.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49')
req.add_header('referer', url)
req.add_header('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng')
req.add_header('Accept-Encoding', 'gzip')

content = urlopen(req).read()

gzip_file = io.BytesIO(content)
with gzip.open(gzip_file, 'rt') as f:
    html_data = f.read()
print(html_data)

with open('output.html', 'w') as output:
    output.write(html_data)

soup = BeautifulSoup(html_data,'html.parser')
dom = etree.HTML(str(soup))
print(dom)
# print(dom.xpath('//*[@id="BGINP01_S1"]/section/div/font/text()'))
print(dom.xpath('//*/h1'))

