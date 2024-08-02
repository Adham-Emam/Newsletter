from apscheduler.schedulers.blocking import BlockingScheduler
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def run_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl("news")
    process.start()


scheduler = BlockingScheduler()
scheduler.add_job(run_spider, "interval", hours=1)
scheduler.start()
