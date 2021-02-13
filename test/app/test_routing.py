
import random
import string
from typing import List
import unittest

from bamboo.app import App
from bamboo.endpoint import Endpoint
from bamboo.location import NumLocation, StringLocation, Uri_t
from bamboo.request import http_get
from bamboo.router import DuplicatedUriRegisteredError, Router
from bamboo.test import ServerForm, TestExecutor


def rand_string(k: int) -> str:
    return "".join(random.choices(string.ascii_letters + string.digits, k=k))


def rand_strings(num: int) -> List[str]:
    return [rand_string(random.randint(10, 20)) for _ in range(num)]


IDEAL_RESNPONSE = "Hello, World".encode()


# Template endpoints
class MockEndpoint(Endpoint):
    
    def do_GET(self) -> None:
        self.send_body(IDEAL_RESNPONSE)
        

class TestRouting(unittest.TestCase):
        
    def test_routing(self):
        # Make different uris
        URIS = list(set(rand_strings(100)))
        
        def client():
            for i, uri in enumerate(URIS):
                res = http_get(f"http://localhost:{8000 + i}/{uri}")
                self.assertEqual(res.body, IDEAL_RESNPONSE)
                
        forms = []
        for i, uri in enumerate(URIS):
            app = App()
            app.route(uri)(MockEndpoint)
            forms.append(ServerForm("", 8000 + i, app, "test_routing.log"))
        
        executor = TestExecutor(client)
        executor.add_forms(*forms)
        executor.exec()
        
    def _test_duplicated_uris(self, patterns: List[Uri_t]):
        router = Router()
        
        with self.assertRaises(DuplicatedUriRegisteredError) as err:
            for uri in patterns:
                router.register(uri, MockEndpoint)
                
        self.assertIsInstance(err.exception, DuplicatedUriRegisteredError)
            
    def test_duplicated_uris(self):
        PATTERNS_1 = [("test", "hoge", StringLocation()),
                      ("test", "hoge", "image")]
        PATTERNS_2 = [(StringLocation(), NumLocation(4)),
                      ("hoge", "hoge")]
        PATTERNS_3 = [(StringLocation(), "test", StringLocation()),
                      ("hoge", StringLocation(), "image")]
        
        self._test_duplicated_uris(PATTERNS_1)
        self._test_duplicated_uris(PATTERNS_2)
        self._test_duplicated_uris(PATTERNS_3)
            

if __name__ == "__main__":
    unittest.main()
