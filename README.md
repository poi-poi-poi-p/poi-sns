# これは何

Django + DRF + PostgreSQLでオレオレFediverseサーバーを作ってみたかったリポジトリ

開発環境は[DevContainer](https://code.visualstudio.com/docs/devcontainers/containers)で作成

# コンテナの作成と起動

```
$ cd poi-sns
$ docker build -f deploy/Dockerfile -t django .
$ docker run -p 8000:8000 -it --rm django
```