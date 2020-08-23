from get_news import GetNews
import slackweb

slack = slackweb.Slack(url="")

getNews = GetNews()
topHeadlines = getNews.getCoronaNews()
if(topHeadlines['totalResults'] > 0):
    attachments = []
    attachment = {
        "title": topHeadlines['articles'][0]['title'],
        "text": "[" + topHeadlines['articles'][0]['url'] + "]"
    }
    attachments.append(attachment)
    slack.notify(attachments=attachments)
else:
    slack.notify(text="本日のコロナ関連ニュースはありません。")
