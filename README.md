# Bamboo

[![Bamboo](docs/res/bamboo.png)](https://jjj999.github.io/bamboo/)
[![PyPI version](https://badge.fury.io/py/bamboo-core.svg)](http://badge.fury.io/py/bamboo-core)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://pypi.python.org/pypi/bamboo-core/)

## Installling
* Python: >= 3.8

```
$ python -m pip install bamboo-core
```

## Usage
詳細なドキュメントは[こちら](https://jjj999.github.io/bamboo/tutrials/concept/)を参照してください．以下は簡単な実装例です．

```python
from bamboo import WSGIApp, WSGIEndpoint, WSGITestExecutor

app = WSGIApp()

@app.route("hello")
class MockEndpoint(WSGIEndpoint):

    def do_GET(self) -> None:
        self.send_body(b"Hello, World!")

if __name__ == "__main__":
    WSGITestExecutor.debug(app, "debug_app.log")
```

上記スクリプトを実行後，ブラウザで http://localhost:8000/hello にアクセスしてみましょう．

## API documentation
Bamboo の API ドキュメントは[こちら](https://jjj999.github.io/bamboo/api/bamboo/)．

## Examples

### [upsidedown](example/upsidedown/)
リクエストされた文字列を逆順に反転させて返すアプリケーションです．

### [image_traffic](example/image_traffic/)
アクセスに対して静的な画像を返すアプリケーションです．

### [tweets](example/tweets/)
CLI ベースの簡易的な Twitter のような投稿アプリです．認証機能は実装されていません．
