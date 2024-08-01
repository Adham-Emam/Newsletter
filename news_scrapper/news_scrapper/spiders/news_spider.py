import os
import scrapy
import json
from urllib.parse import urlparse
from constants import URLS, ARTICLE_LINK_SELECTORS, TITLE_SELECTORS, LAST_UPDATED_SELECTORS, IMG_URL_SELECTORS, BODY_CONTENT_SELECTORS


class NewsSpider(scrapy.Spider):
    name = "news"
    articles = []

    def start_requests(self):
        self.start_urls = URLS

        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse_homepage)

    def parse_homepage(self, response):
        article_links = response.css(ARTICLE_LINK_SELECTORS).getall()
        for link in article_links:
            yield response.follow(url=link, callback=self.parse_article)

    def parse_article(self, response):
        # Extract items from Given URL
        title = response.css(TITLE_SELECTORS).get()
        last_updated = response.css(LAST_UPDATED_SELECTORS).get()
        img_url = response.css(IMG_URL_SELECTORS).get()
        body_parts = response.css(BODY_CONTENT_SELECTORS).getall()
        # Join all text parts to form the complete body text
        body = "".join(body_parts)

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
