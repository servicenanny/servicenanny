import collections
import hashlib
import hmac
import json
import re
from copy import deepcopy
from urllib.parse import parse_qsl


class ProdamusVerificate:
    def verify(self, sign: str, body: bytes, secret_key: str):
        expected_signature = hmac.new(secret_key.encode(), body, hashlib.sha256).hexdigest()
        result = hmac.compare_digest(sign, expected_signature)
        return result