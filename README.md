# iSpanish

## How to set up
Please install docker in ur laptop

clone code from GitHub

```
git clone https://github.com/Tapioca-Engineer/Brown.git
```

And I(Kanta) give u a .env file

And type next command in the iSpanish/iSpanish/.

Docker build

```
docker-compose build
```

Docker up

```
docker-compose up
```

server start

```
http://0.0.0.0:8000/
```

open container
```
docker exec -it iSpanish_web /bin/bash
```

makemigrations
```
python manage.py makemigrations
```

migrate
```
python manage.py migrate
```
