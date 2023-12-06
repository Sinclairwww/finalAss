from finalAss.spiders import basicSpider


class ShSpider(basicSpider.BasicSpider):
    name = "sh"
    allowed_domains = ["sh.lianjia.com"]
    start_urls = ["https://sh.lianjia.com/zufang/jingan/",
                  "https://sh.lianjia.com/zufang/huangpu/",
                  "https://sh.lianjia.com/zufang/xuhui/",
                  "https://sh.lianjia.com/zufang/changning/",
                  "https://sh.lianjia.com/zufang/putuo/",
                  "https://sh.lianjia.com/zufang/baoshan/",
                  "https://sh.lianjia.com/zufang/minhang/",
                  "https://sh.lianjia.com/zufang/jiading/",
                  "https://sh.lianjia.com/zufang/pudongxinqu/",
                  "https://sh.lianjia.com/zufang/jinshan/",
                  "https://sh.lianjia.com/zufang/songjiang/",
                  "https://sh.lianjia.com/zufang/qingpu/",
                  "https://sh.lianjia.com/zufang/fengxian/",
                  "https://sh.lianjia.com/zufang/chongming/",
                  "https://sh.lianjia.com/zufang/fengxian/",
                  "https://sh.lianjia.com/zufang/songjiang/",
                  "https://sh.lianjia.com/zufang/qingpu/",
                  ]
    prefix = "https://sh.lianjia.com/zufang/"
    index = {
        "jingan": 2,
        "huangpu": 2,
        "xuhui": 2,
        "changning": 2,
        "putuo": 2,
        "baoshan": 2,
        "minhang": 2,
        "jiading": 2,
        "pudongxinqu": 2,
        "jinshan": 2,
        "songjiang": 2,
        "qingpu": 2,
        "fengxian": 2,
        "chongming": 2,
        "fengxian": 2,
        "songjiang": 2,
        "qingpu": 2,
    }
