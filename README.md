# A-Soul Meme

## 命令行运行

```shell
.
├── api.py                      # api文件
├── art_detail.py               # 图片获取
├── art_list.py					# 专栏获取
├── db.py						# 数据库
├── docker-compose.yml
├── Dockerfile
├── example.db					# db
├── LICENSE
├── README.md
└── requirements.txt			# 依赖
```

### 初始化数据库

`python3 db.py`

### 爬取专栏

`python3 art_list.py`

### 爬取专栏内图片

`python3 art_detail.py`

### 启动API服务

`python3 api.py`

## 镜像运行

镜像仓库: `https://hub.docker.com/r/gsxhnd/asoul-meme`

### docker-compose运行服务

```yaml
version: "3"

services:
  meme:
    container_name: meme
    image: gsxhnd/asoul-meme:version-0.0.5
    ports:
      - "8000:8000"
    command: python3 /app/api.py
```

## 获取图片列表接口接口

```http
GET /
```

| Query 参数 | 必选 | 说明     |
| :--------- | :--- | -------- |
| limit      | true | 限制个数 |
| page       | true | 页面     |

接口示例

```http
GET /?page=1&limit=5
```

```json
// 请求内容
{}
```

```json
// 返回内容
{
  "code": 0,
  "data": [
    {
      "id": 679,
      "url": "i0.hdslb.com/bfs/article/875f3725e7f5835abf2cf9b38c6b7c887932467e.jpg"
    },
    {
      "id": 678,
      "url": "i0.hdslb.com/bfs/article/1edb2b115d7bfa63cfc56687c40c36df2383b83f.jpg"
    },
    {
      "id": 677,
      "url": "i0.hdslb.com/bfs/article/21b488448b070500769efec0477a1ab6ddccef7f.jpg"
    },
    {
      "id": 676,
      "url": "i0.hdslb.com/bfs/article/ea087243ef5342880f9ef1cf156be5d7c6d6dbaa.jpg"
    },
    {
      "id": 675,
      "url": "i0.hdslb.com/bfs/article/e23169e1c6c8d5a365019d3ebafc19b321065e43.jpg"
    }
  ],
  "message": "success"
}
```
