class UrlManager():
    """
    UrlManager
    管理爬取过的url以及等待爬取的url
    将url分为两个集合，new_url为等待爬取的url，old_url为爬取过的url
    从new_url中取出一个url进行爬取并将其加入old_url
    """
    def __init__(self):
        self.new_url = set()
        self.old_url = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_url and url not in self.old_url:
            self.new_url.add(url)

    # 返回集合的长度
    def new_url_len(self):
        return len(self.new_url)!=0


    # 将解析出来并存储在列表中的url添加到集合中
    def add_new_urls(self, urls):
        for url in urls:
            self.add_new_url(url)


     # 从集合中取出一个url开始爬取并将其加入到old_url集合
    def craw_url(self):
        craw_url = self.new_url.pop()
        self.old_url.add(craw_url)
        return craw_url
