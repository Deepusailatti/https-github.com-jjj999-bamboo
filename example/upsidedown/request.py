
import sys

from bamboo.api import JsonApiData
from bamboo.request import http


class UpsideDownResponse(JsonApiData):
    
    result: str
    

def request(uri: str, token: str) -> None:
    body = {"token": token}
    res = http.get(uri, json=body, datacls=UpsideDownResponse)
    
    print("Headers")
    print("-------")
    for k, v in res.headers.items():
        print(f"{k} : {v}")
    print()
    
    body = res.attach()
    print("Bodies")
    print("------")
    print(body.result)
    
if __name__ == "__main__":
    URI = "http://localhost:8000/upsidedown"
    token = sys.argv[1]
    request(URI, token)