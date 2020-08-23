from newsapi import NewsApiClient

class GetNews:
    
    def __init__(self):
        # News APIで発行したキーを指定
        self.newsapi = NewsApiClient(api_key='')
    def getCoronaNews(self):
        topHeadlines = self.newsapi.get_top_headlines(q='新型コロナ', country='jp')
        return topHeadlines
