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

### 启动 API 服务

`python3 api.py`

## 镜像运行

镜像仓库: `https://hub.docker.com/r/gsxhnd/asoul-meme`

### docker-compose 运行服务

```yaml
version: "3"

services:
  meme:
    container_name: meme
    image: gsxhnd/asoul-meme:version-0.1.0
    ports:
      - "8000:8000"
    command: python3 /app/api.py
```

## 获取图片列表接口接口

```http
GET /
```

| Query 参数 | 必选 | 说明                                          |
| :--------- | :--- | --------------------------------------------- |
| limit      | true | 限制个数                                      |
| page       | true | 页面                                          |
| order_by   | true | 排序健，用`,`分割，支持 `width`,`height`,`id` |
| sort_by    | true | 排序类型升序或降序，用`,`分割，`asc`或`desc`  |

| 返回字段 | 字段类型 | 说明         |
| :------- | :------- | :----------- |
| id       | `int`    | id           |
| url      | `string` | cdn 地址     |
| height   | `int`    | 图片实际高度 |
| width    | `int`    | 图片实际宽度 |

接口示例

```http
GET /?page=1&limit=5&order_by=width,height,id&sort_by=desc,asc,asc
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
      "height": 2000,
      "id": 535,
      "url": "i0.hdslb.com/bfs/article/92754e3274ae57fe4dfebfc1e76048d38abbcf18.jpg",
      "width": 2000
    },
    {
      "height": 922,
      "id": 126,
      "url": "i0.hdslb.com/bfs/article/7a4dbb3c359a4287158148da63d2ed9c25a1e884.jpg",
      "width": 1920
    },
    {
      "height": 1080,
      "id": 160,
      "url": "i0.hdslb.com/bfs/article/b3f29da3bae582d1f57c1ab554b02b3d12806be9.jpg",
      "width": 1728
    },
    {
      "height": 968,
      "id": 385,
      "url": "i0.hdslb.com/bfs/article/813066217a3095ce1f4c315bb3c86bfc7d90747a.jpg",
      "width": 1726
    },
    {
      "height": 1640,
      "id": 542,
      "url": "i0.hdslb.com/bfs/article/5f23dfa72154ae7fb82bcc0ce1be799c9d612b0c.jpg",
      "width": 1640
    }
  ],
  "message": "success"
}
```
