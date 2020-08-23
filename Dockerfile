#PythonのDockerイメージを指定
FROM python:3.7.3

# 必要なライブラリインストール
RUN pip install newsapi-python
RUN pip install slackweb

WORKDIR /app
COPY . /app
