# salck-news-bot  
### clone  
https://github.com/ay-nakamura/slack-news-bot.git

### newsAPIのキーを指定
1. 下記からnewsAPIのkeyを取得
https://newsapi.org/docs/get-started
2. 下記に取得したkeyを指定
```
self.newsapi = NewsApiClient(api_key='')
```

### Slackの投稿用URLを発行
1. 下記から投稿用URLを発行
https://my.slack.com/services/new/incoming-webhook/
2. 下記に取得したURLを指定
```
slack = slackweb.Slack(url="")
```

### イメージ作成  
cd ${Dockerファイルの存在するパス}  
docker build -t app --no-cache .  

### コンテナ起動  
#### 本番環境用  
docker run -it -d --name slack_bot app bash  
#### 開発環境用（マウントあり）  
docker run -it -d --name slack_bot -v ${slack-news-botの存在する絶対パス}/slack-news-bot:/app app bash
### 実行コマンド  
docker exec slack_bot python send_to_slack.py
