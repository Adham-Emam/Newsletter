import scrapy
import json
from urllib.parse import urlparse


class NewsSpider(scrapy.Spider):
    name = "news"
    articles = []

    def start_requests(self):
        self.start_urls = [
            # "takeitright2022.com",
            "https://trends.khbrny.com/",
            "https://highwia.com/",
            # "https://www.syriamatrix.com/",
            # "https://ww.kuwaitpress.net",
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
            # 'https://www.kooora.com/',
            # 'https://mj.bald-news.com/',
            # 'https://www.arabiaweather.com/',
            # 'https://mesrena.com/',
            # 'https://m.sa24.co/'
        ]

        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse_homepage)

    def parse_homepage(self, response):
        article_links = response.css("a.post-thumb::attr(href)").getall()

        for link in article_links:
            yield response.follow(url=link, callback=self.parse_article)

    def parse_article(self, response):
        title = response.css("h1.post-title::text").get()
        last_updated = response.css("span.last-updated::text").get()
        img_url = response.css("img.wp-post-image::attr(src)").get()
        body = "".join(response.css("div.entry-content p::text").getall())

        # Format the data as a string
        article_data = {
            "url": response.url,
            "title": title,
            "last_updated": last_updated,
            "image_url": img_url,
            "body": body,
        }

        self.articles.append(article_data)

    def closed(self, reason):
        # Prepare data for JSON serialization
        data = {"articles": self.articles}

        # Write data to JSON file
        filename = "data.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.articles, f, ensure_ascii=False, indent=4)
        self.log(f"Saved {len(self.articles)} articles to {filename}")
