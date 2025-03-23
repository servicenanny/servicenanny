import collections
from typing import MutableMapping
import json
import hmac
import hashlib


class ProdamusVerificate:
    def __init__(self, secret: str):
        self.__secret = secret
        
    def sign(self, data: dict) -> str:
        # переводим все значения data в string c помощью кастомной функции deep_int_to_string (см ниже)
        self.deep_int_to_string(data)
        # переводим data в JSON, с сортировкой ключей в алфавитном порядке, без пробелом и экранируем бэкслеши
        data_json = json.dumps(data, sort_keys=True, ensure_ascii=False, separators=(',', ':')).replace("/", "\\/")
        # создаем подпись с помощью библиотеки hmac и возвращаем ее
        return hmac.new(self.__secret.encode('utf8'), data_json.encode('utf8'), hashlib.sha256).hexdigest()

    def deep_int_to_string(self, dictionary: dict):
        for key, value in dictionary.items():
            if isinstance(value, MutableMapping):
                self.deep_int_to_string(value)
            elif isinstance(value, list) or isinstance(value, tuple):
                for k, v in enumerate(value):
                    self.deep_int_to_string({str(k): v})
            else: dictionary[key] = str(value)

    def verify(self, obj: dict, sign: str):
        expected_sign = self.sign(obj)
        return expected_sign and (expected_sign.lower() == sign.lower())