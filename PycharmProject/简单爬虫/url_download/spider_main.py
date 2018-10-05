
from url_download import url_manager, html_downloader, html_parser, html_output


class SpiderMain():
    '''
    总调度器
    实现程序的总体调度

    '''
    def __init__(self):

        '''
        初始化
        定义所需要的url管理器
        定义所需要的html下载器
        定义所需要的html解析器
        定义所需要的html输出器
        '''

        self.url_manager = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_output.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.url_manager.add_new_url(root_url)
        while self.url_manager.new_url_len():
            try:
                new_url = self.url_manager.craw_url()
                print("craw%d: %s"%(count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.url_manager.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 1000:
                    break
                count += 1
            except:
                print("craw failed")
        self.outputer.output_html()


if __name__ == "__main__":

    root_url = "https://baike.baidu.com/item/Python"
    spider = SpiderMain()
    spider.craw(root_url)
