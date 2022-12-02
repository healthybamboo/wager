# Python用のDockerfile
FROM python:3.9
USER root
EXPOSE 8000

# ベースイメージに対してコマンドを実行
RUN apt-get update && apt-get install -y \
    vim \
    less \
    git \
    && rm -rf /var/lib/apt/lists/*

# 環境変数に値をセット
ENV LANG C.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9


# requirements.txtをコピー
COPY requirements.txt /home/wager/

# 初期化用のスクリプトをコピー
COPY init.sh /script/
COPY wait-for-it.sh /script/

# ワーキングディレクトリを指定
WORKDIR /home/wager


# ライブラリをインストール
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
