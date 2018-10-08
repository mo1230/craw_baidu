"""
用来管理url
将所找到的url组成一个集合（可以过滤掉重复的url）

"""

class UrlManage():
    """
    功能：
        - 将url组成一个集合
        - 将一个url从集合取出进行爬取
        - 将新的url加入集合

    """

    def __init__(self):
        self.urls = set()
        self.old_urls = set()  # 将爬取过的url存放于old_urls

    def add_urls(self, url):
        """
        如果一个url既不在urls集合中，又不在old_urls集合中，则将其加入到urls集合中

        :param url:
        :return:
        """
        if url not in self.urls and url not in self.old_urls:
            self.urls.add(url)
        return None

    def add_monay_urls(self, url_list):

        for url1 in url_list:
            self.urls.add(url1)

    def craw_url(self):
        """
        从urls集合中取出一个url，并将其加入到old_urls集合
        :return:
        """
        crawing_url = self.urls.pop()
        self.old_urls.add(crawing_url)
        return crawing_url
