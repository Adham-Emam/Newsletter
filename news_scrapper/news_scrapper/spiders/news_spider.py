import re
from pathlib import Path


import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'

    def start_requests(self):
        urls = [
'https://trends.khbrny.com/',
# 'https://highwia.com/',
# 'https://www.syriamatrix.com/',
# 'https://ww.kuwaitpress.net',
# 'https://zawayan.com',
# 'https://newso.elsob7.com/',
# 'https://www.sayidaty.net/',
# 'https://mj.bald-news.com/',
# 'https://trend.nl7za.com/',
# 'https://clubtc.net',
# 'https://m.sa24.co/',
# 'https://almontag.com/',
# 'https://www.yanba7.com/',
# 'https://m.sa24.co/',
# 'https://wikieurope.net/',
# 'https://molhamon.com',
# 'https://arabic.sport360.com/',
# 'https://sa.tqwem.com/',
# 'https://mesrena.com/',
# 'https://www.masrawy.com/',
# 'https://www.elbalad.news/',
# 'https://ar.ra2ya.com/',
# 'https://alhkaia.com/',
# 'https://royanews.tv/',
# 'https://aramland.com/',
# 'https://arab.sahafahh.net/',
# 'https://mz-mz.net/',
# 'https://m.sa24.co/',
# 'https://app.lesite24.com/',
# 'https://mostakpel.com/',
# 'https://www.kooora.com/',
# 'https://www.youm7.com/',
# 'https://mesrena.com/',
# 'https://www.thaqfny.com/',
# 'https://www.yallakora.com/',
# 'https://gate.ahram.org.eg/',
# 'https://m.sa24.co/',
# 'https://www.webteb.com/',
# 'https://mawdoo3.com/',
# 'https://mhtwyat.com/',
# 'https://news.faharas.net/',
# 'https://www.khaberni.com/',
# 'https://shbabbek.com/',
# 'https://mobizil.com/',
# 'https://jo.motory.com/ar/',
# 'https://altibbi.com/',
# 'https://jordanrec.com/',
# 'https://shootz.yalla-shoot-tv.live/home18/',
# 'https://misr-post.com/',
# 'https://newso.elsob7.com/',
# 'https://sa.tqwem.com/',
'https://www.kooora.com/',
# 'https://mj.bald-news.com/',
# 'https://www.arabiaweather.com/',
# 'https://mesrena.com/',
# 'https://m.sa24.co/'
]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

        
    def parse(self, response):
        regex = r"(?:https?:\/\/)?(?:www\.)?([a-zA-Z0-9-]+)\.[a-zA-Z]{2,}(?:\/|$)"
        domain_name = response.url.split("/")[-2]
        match = re.search(regex, domain_name)
        if match:
            filename = f"{match.group(1)}.html"
            Path(filename).write_bytes(response.body)
            self.log(f"Saved file {filename}")