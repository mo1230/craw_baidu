
# -*-coding:utf-8-*-


import url_manage, outputer, html_parser


class Main():
    def __init__(self):
        self.url_manager = url_manage.UrlManage()
        self.output = outputer.Outputer()
        self.soup = html_parser.HtmlParser()

    def craw(self, root_url):
        self.url_manager.add_urls(root_url)

        count = 1
        while len(self.url_manager.urls):
            try:
                # 从urls集合中取出一个url
                new_url = self.url_manager.craw_url()

                print("url%s  " % count, new_url)

                # 解析url指向的页面,解析器可以获取新的url
                new_monay_urls1 = self.soup.parser(new_url)

                self.url_manager.add_monay_urls(new_monay_urls1)
                self.output.collect_data(new_url)
                count += 1
                if count > 1000:
                    break
            except:
                print("craw failed")
        # 将所爬取的url输出
        self.output.html_output()


if __name__ == "__main__":
    root_url = "https://www.bilibili.com"
    main = Main()
    main.craw(root_url)






