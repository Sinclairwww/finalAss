from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor
from lianjia.spiders.ESFHouse import ESFHouseSpider
from lianjia.spiders.NewHouse import NewHouseSpider
from scrapy.utils.project import get_project_settings

configure_logging()
settings = get_project_settings()
runner = CrawlerRunner(settings)
runner.crawl(NewHouseSpider)
# runner.crawl(ESFHouseSpider)
d = runner.join()
d.addBoth(lambda _: reactor.stop())
reactor.run()  # the script will block here until the crawling is finished


commandline.execute("scrapy crawl NewHouseSpider".split())

//开始爬取
scrapy crawl NewHouseSpider


//命令行执行

scrapy crawl NewHouseSpider -o newHouse.json