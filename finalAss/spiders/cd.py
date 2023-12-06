from finalAss.spiders import basicSpider


class GzSpider(basicSpider.BasicSpider):
    name = "cd"
    allowed_domains = ["cd.lianjia.com"]
    start_urls = [
        "https://cd.lianjia.com/zufang/jinjiang/",
        "https://cd.lianjia.com/zufang/qingyang/",
        "https://cd.lianjia.com/zufang/wuhou/",
        "https://cd.lianjia.com/zufang/gaoxin7/",
        "https://cd.lianjia.com/zufang/chenghua/",
        "https://cd.lianjia.com/zufang/jinniu/",
        "https://cd.lianjia.com/zufang/tianfuxinqu/"
        "https://cd.lianjia.com/zufang/gaoxinxi/",
        "https://cd.lianjia.com/zufang/shuangliu/",
        "https://cd.lianjia.com/zufang/wenjiang/",
        "https://cd.lianjia.com/zufang/pidou/",
        "https://cd.lianjia.com/zufang/longquanyi/"
        "https://cd.lianjia.com/zufang/xindou/",
        "https://cd.lianjia.com/zufang/qingbaijiang/",
        "https://cd.lianjia.com/zufang/jianyang/",
    ]
    index = {
        "jinjiang": 2,
        "qingyang": 2,
        "wuhou": 2,
        "gaoxin7": 2,
        "chenghua": 2,
        "jinniu": 2,
        "tianfuxinqu": 2,
        "gaoxinxi": 2,
        "shuangliu": 2,
        "wenjiang": 2,
        "pidou": 2,
        "longquanyi": 2,
        "xindou": 2,
        "qingbaijiang": 2,
        "jianyang": 2,
    }
    prefix = "https://cd.lianjia.com/zufang/"
