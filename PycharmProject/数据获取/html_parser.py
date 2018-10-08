from bs4 import BeautifulSoup as bs
import re
from urllib import request, parse


class HtmlParser():
    def parser(self, url):
        url0 = request.urlopen(url).read().decode("utf-8")

        links = set()
        soup = bs(url0, "html.parser")
        link1 = soup.find_all("a", href=re.compile(r"/video/av\w"))
        for link in link1:

            # ！！！！
            new_link = link['href']
            new_full_link = parse.urljoin("https://www.bilibili.com", new_link)
            links.add(new_full_link)

        return links

