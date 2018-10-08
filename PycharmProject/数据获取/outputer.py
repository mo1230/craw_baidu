

class Outputer():
    """
    将所爬取的url形成一个html文档
    """
    def __init__(self):
        self.data = []

    def collect_data(self, url):
        self.data.append(url)

    def html_output(self):
        file = open("bilibili_music.html", "w", encoding="utf-8")
        file.write("<html>")
        file.write("<head>")
        file.write("<meta charset=utf-8 />")
        file.write("</head>")

        file.write("<body>")

        for datas in self.data:
            file.write("%s<br />"%datas)


        file.write("</body>")

        file.write("</html>")

        file.close()