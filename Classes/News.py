import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

class News:
    def GetTopNews(self):
        news_url="https://news.google.com/news/rss"
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()  
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        # Print news title, url and publish date
        i=0
        Allnews = ''
        for news in news_list[:5]:
            i +=1 
            news = str(news.title.text)
            # news=news.replace("-", "\n\tNews by")
            Allnews = Allnews + "News " + str(i) +" " + news + "\n"
        print(Allnews)
        return(Allnews)

# N = News()
# N.GetTopNews()