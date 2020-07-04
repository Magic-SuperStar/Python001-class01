学习笔记  
### maoyan 使用requests/BeautifulSoup/lxml.etree.xpath
#### 问题1：
* 模拟浏览器打开<https:maoyan.com/films?showType=2>(想着以为是反爬虫的问题)  
要headers['user-agent']:'Mozilla/4.0 ......' 用的是本开发电脑的浏览器的user-agent  
一时可以一时不行
####  问题2：
* 使用lxml.etree.xpath的语法问题’div[@class="movie-brief-container"]..‘前面缺少’//‘  
导致xpath找不到对应元素  
#### 问题3：
* lxml.etree.xpath返回的是数组集合  
出现外循环的数组无法append()  
问题4：还有就是url拼接问题
