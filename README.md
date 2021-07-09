# tweet-watcher

![Untitled Diagram(15)](https://user-images.githubusercontent.com/51913879/125141423-ff7d4d80-e14f-11eb-81ef-46b7234025d5.png)

とあるユーザーのTwitterアカウントを監視しながら特定のキーワードを含むツイートに反応して何らかのアクションを実行するサンプルコード。詳細はQiitaにて記載。

https://qiita.com/kazama1209/items/8db398e0948dbb4ae63d

## セットアップ

環境変数をセット。

```
$ cp .env.sample .env

TWITTER_API_KEY=
TWITTER_API_SECRET=
TWITTER_ACCESS_TOKEN=
TWITTER_ACCESS_TOKEN_SECRET=
TWITTER_USER_ID=
```

コンテナを起動。

```
$ docker-compose up -d
```

コードを実行。

```
$ docker-compose run python3 python main.py
```
