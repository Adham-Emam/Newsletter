import os
import scrapy
import json
from urllib.parse import urlparse


class NewsSpider(scrapy.Spider):
    name = "news"
    articles = []

    def start_requests(self):
        self.start_urls = [
            "https://alhkaia.com/",
            "https://almontag.com/",
            "https://altibbi.com/",
            "https://app.lesite24.com/",
            "https://ar.ra2ya.com/",
            "https://arab.sahafahh.net/",
            "https://arabic.sport360.com/",
            "https://aramland.com/",
            "https://clubtc.net",
            "https://gate.ahram.org.eg/",
            "https://highwia.com/",
            "https://jo.motory.com/ar/",
            "https://jordanrec.com/",
            "https://m.sa24.co/",
            "https://mawdoo3.com/",
            "https://mesrena.com/",
            "https://mhtwyat.com/",
            "https://misr-post.com/",
            "https://mj.bald-news.com/",
            "https://mobizil.com/",
            "https://molhamon.com",
            "https://mostakpel.com/",
            "https://mz-mz.net/",
            "https://news.faharas.net/",
            "https://newso.elsob7.com/",
            "https://royanews.tv/",
            "https://sa.tqwem.com/",
            "https://shbabbek.com/",
            "https://shootz.yalla-shoot-tv.live/home18/",
            "https://takeitright2022.com",
            "https://trend.nl7za.com/",
            "https://trends.khbrny.com/",
            "https://wikieurope.net/",
            "https://ww.kuwaitpress.net",
            "https://www.arabiaweather.com/",
            "https://www.elbalad.news/",
            "https://www.khaberni.com/",
            "https://www.kooora.com/",
            "https://www.masrawy.com/",
            "https://www.sayidaty.net/",
            "https://www.syriamatrix.com/",
            "https://www.thaqfny.com/",
            "https://www.webteb.com/",
            "https://www.yallakora.com/",
            "https://www.yanba7.com/",
            "https://www.youm7.com/",
            "https://zawayan.com",
        ]

        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse_homepage)

    def parse_homepage(self, response):
        article_links = response.css(
            "a.post-thumb::attr(href), "
            "a.post-link::attr(href), "
            "a.article-link::attr(href), "
            "a.entry-link::attr(href), "
            "a.news-link::attr(href), "
            "a.link::attr(href), "
            "a.item-link::attr(href), "
            "a.post::attr(href), "
            "a.headline-link::attr(href), "
            "a.read-more::attr(href), "
            "a.story-link::attr(href), "
            "a.content-link::attr(href), "
            "a.featured-link::attr(href), "
            "a.latest-link::attr(href), "
            "a[data-article-link]::attr(href), "
            "a[data-link]::attr(href)"
        ).getall()

        for link in article_links:
            yield response.follow(url=link, callback=self.parse_article)

    def parse_article(self, response):
        # Extract title
        title = response.css(
            "h1.post-title::text, "
            "h1.article-title::text, "
            "h1.entry-title::text, "
            "h1.headline-title::text, "
            "h1.news-title::text, "
            "h1.title::text, "
            "h1.page-title::text"
        ).get()

        # Extract last updated timestamp
        last_updated = response.css(
            "span.last-updated::text, "
            "span.time-updated::text, "
            "span.updated::text, "
            "span.date-updated::text, "
            "span.timestamp::text, "
            "span.publish-date::text, "
            "span.modified-date::text"
        ).get()

        # Extract image URL
        img_url = response.css(
            "img.wp-post-image::attr(src), "
            "img.wp-post-image::attr(srcset), "
            "img.article-image::attr(src), "
            "img.featured-image::attr(src), "
            "img.main-image::attr(src), "
            "img.primary-image::attr(src), "
            "img.image::attr(src)"
        ).get()

        # Extract body text
        body_parts = response.css(
            "div.entry-content p::text, "
            "div.entry-content ol::text, "
            "div.article-content p::text, "
            "div.article-content ol::text, "
            "div.content p::text, "
            "div.content ol::text, "
            "div.main-content p::text, "
            "div.main-content ol::text, "
            "div.post-content p::text, "
            "div.post-content ol::text"
        ).getall()
        body = "".join(body_parts)  # Join all text parts to form the complete body text

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
        data = {"articles": self.articles}

        # Write data to JSON file
        filename = "data.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.articles, f, ensure_ascii=False, indent=4)
        self.log(f"Saved {len(self.articles)} articles to {filename}")
