from finalAss.spiders import basicSpider


class SzSpider(basicSpider.BasicSpider):
    name = "sz"
    allowed_domains = ["sz.lianjia.com"]
    start_urls = [
        "https://sz.lianjia.com/zufang/luohuqu/",
        "https://sz.lianjia.com/zufang/futianqu/",
        "https://sz.lianjia.com/zufang/nanshanqu/",
        "https://sz.lianjia.com/zufang/yantianqu/",
        "https://sz.lianjia.com/zufang/baoanqu/",
        "https://sz.lianjia.com/zufang/longgangqu/",
        "https://sz.lianjia.com/zufang/longhuaqu/",
        "https://sz.lianjia.com/zufang/guangmingqu/",
        "https://sz.lianjia.com/zufang/pingshanqu/",
        "https://sz.lianjia.com/zufang/dapengxinqu/",
    ]
    index = {
        "luohuqu": 2,
        "futianqu": 2,
        "nanshanqu": 2,
        "yantianqu": 2,
        "baoanqu": 2,
        "longgangqu": 2,
        "longhuaqu": 2,
        "guangmingqu": 2,
        "pingshanqu": 2,
        "dapengxinqu": 2,
    }
    prefix = "https://sz.lianjia.com/zufang/"
