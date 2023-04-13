# iSpanish

## 動作環境
- Docker 

## Setup

Gitからコードをクローン

```
git clone https://github.com/Tapioca-Engineer/Brown.git
```

Notionのdocumentにある.envをコピーしroot直下に.envを作成

Docker build

```
docker-compose build
```

Docker 起動

```
docker-compose up
```

アクセス

```
http://0.0.0.0:8000/
```

Dockerコンテナ内のBashシェルを起動
```
docker exec -it brown_web /bin/bash
```
