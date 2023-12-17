# これは何

Django + DRF + PostgreSQLでオレオレFediverseサーバーを作ってみたかったリポジトリ

開発環境は[DevContainer](https://code.visualstudio.com/docs/devcontainers/containers)で作成

# 使い方

```
リポジトリのクローン
$ git clone git@github.com:poi-poi-poi-p/poi-sns.git
$ cd poi-sns

.env.sampleに従って環境変数を設定する
$ vi .env

コンテナのビルドと実行
$ docker build -f deploy/Dockerfile -t django .
$ docker run -p 8000:8000 -it --rm django

ブラウザで http://127.0.0.1:8000 を開く
```
