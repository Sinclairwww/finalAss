from finalAss.spiders import basicSpider


class BjSpider(basicSpider.BasicSpider):
    name = "bj"
    allowed_domains = ["bj.lianjia.com"]
    start_urls = [
        "https://bj.lianjia.com/zufang/dongcheng/",
        "https://bj.lianjia.com/zufang/xicheng/",
        "https://bj.lianjia.com/zufang/chaoyang/",
        "https://bj.lianjia.com/zufang/haidian/",
        "https://bj.lianjia.com/zufang/fengtai/",
        "https://bj.lianjia.com/zufang/shijingshan/",
        "https://bj.lianjia.com/zufang/tongzhou/",
        "https://bj.lianjia.com/zufang/changping/",
        "https://bj.lianjia.com/zufang/daxing/",
        "https://bj.lianjia.com/zufang/yizhuangkaifaqu/",
        "https://bj.lianjia.com/zufang/shunyi/",
        "https://bj.lianjia.com/zufang/fangshan/",
        "https://bj.lianjia.com/zufang/mentougou/",
        "https://bj.lianjia.com/zufang/pinggu/",
        "https://bj.lianjia.com/zufang/huairou/",
        "https://bj.lianjia.com/zufang/miyun/",
        "https://bj.lianjia.com/zufang/yanqing/",
    ]
    index = {
        "dongcheng": 2,
        "xicheng": 2,
        "chaoyang": 2,
        "haidian": 2,
        "fengtai": 2,
        "shijingshan": 2,
        "tongzhou": 2,
        "changping": 2,
        "daxing": 2,
        "yizhuangkaifaqu": 2,
        "shunyi": 2,
        "fangshan": 2,
        "mentougou": 2,
        "pinggu": 2,
        "huairou": 2,
        "miyun": 2,
        "yanqing": 2,
    }
    prefix = "https://bj.lianjia.com/zufang/"
