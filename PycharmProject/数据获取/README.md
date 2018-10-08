## 爬取bilibili网站所有音乐链接

-----------------

- 组成部分
    - 总控制台
        - 用于控制url管理器以及outputer
    - url管理器
        - 将已有url以及新的url组成一个集合
        - 从集合中取出url进行数据爬取
    - html解析器
        - 利用bs4库解析html文档
    - outputer
        - 将爬取到的url形成一个html文档输出
    
    
    
    
    
### 总结
- 对简单爬虫的组成的理解

> 简单的网络爬虫，使用urllib库中的相关模块将会访问指定的url，并且形成html文件，然后使用beautifulsoup4中的相关类对html文件进行解析，从中提取出相关数据
- 遇到的错误
    - 在使用解析器前没有先使用urllib库对指定url进行访问
    
    