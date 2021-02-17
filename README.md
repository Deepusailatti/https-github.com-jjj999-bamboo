# bamboo

## Installling

* Python: >= 3.8

```
$ python -m pip install git+https://github.com/jjj999/bamboo.git
```

## Usage
詳細なドキュメントは[こちら](./docs/usage/)を参照してください．以下は簡単な実装例です．

```python
from wsgiref.simple_server import make_server

from bamboo import App, Endpoint

app = App()

@app.route("hello")
class MockEndpoint(Endpoint):

    def do_GET(self) -> None:
        self.send_body(b"Hello, World!")

if __name__ == "__main__":
    server = make_server("", 8000, app)
    try:
        print("Hosting on port 8000...")
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print()
```

実行後，ブラウザで http://localhost:8000/hello にアクセスしてみましょう．

## Examples

### [upsidedown](./example/upsidedown/)
リクエストされた文字列を逆順に反転させて返すアプリケーションです．

### [image_traffic](./example/image_traffic/)
アクセスに対して静的な画像を返すアプリケーションです．

### [tweets](./example/tweets)
CLI ベースの簡易的な Twitter のような投稿アプリです．認証機能は実装されていません．