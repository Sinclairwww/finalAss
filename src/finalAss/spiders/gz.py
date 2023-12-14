from finalAss.spiders import basicSpider


class GzSpider(basicSpider.BasicSpider):
    name = "gz"
    allowed_domains = ["gz.lianjia.com"]
    start_urls = [
        "https://gz.lianjia.com/zufang/tianhe/",
        "https://gz.lianjia.com/zufang/yuexiu/",
        "https://gz.lianjia.com/zufang/liwan/",
        "https://gz.lianjia.com/zufang/haizhu/",
        "https://gz.lianjia.com/zufang/panyu/",
        "https://gz.lianjia.com/zufang/baiyun/",
        "https://gz.lianjia.com/zufang/huangpugz/",
        "https://gz.lianjia.com/zufang/conghua/",
        "https://gz.lianjia.com/zufang/zengcheng/",
        "https://gz.lianjia.com/zufang/huadou/",
        "https://gz.lianjia.com/zufang/nansha/",
    ]
    index = {
        "tianhe": 2,
        "yuexiu": 2,
        "liwan": 2,
        "haizhu": 2,
        "panyu": 2,
        "baiyun": 2,
        "huangpugz": 2,
        "conghua": 2,
        "zengcheng": 2,
        "huadou": 2,
        "nansha": 2,
    }
    prefix = "https://gz.lianjia.com/zufang/"
