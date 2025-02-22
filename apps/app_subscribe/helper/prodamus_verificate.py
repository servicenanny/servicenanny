import hmac
import hashlib
import json
from typing import Union, Dict, List


class ProdamusVerificate:
    @staticmethod
    def create(data: Union[Dict, List], key: str, algo: str = 'sha256') -> Union[str, bool]:
        # Проверяем, поддерживается ли алгоритм
        if algo not in hashlib.algorithms_available:
            return False

        # Приводим данные к строковому виду
        def stringify(value):
            if isinstance(value, (dict, list)):
                return {k: stringify(v) for k, v in value.items()} if isinstance(value, dict) else [stringify(v) for v in value]
            return str(value)

        data = stringify(data)
        # Сортируем данные
        ProdamusVerificate._sort(data)
        # Преобразуем данные в JSON-строку
        data_json = json.dumps(data, ensure_ascii=False, separators=(',', ':'))

        # Создаем HMAC-хэш
        hmac_hash = hmac.new(key.encode('utf-8'), data_json.encode('utf-8'), getattr(hashlib, algo))
        return hmac_hash.hexdigest()

    @staticmethod
    def verify(data: Union[Dict, List], key: str, sign: str, algo: str = 'sha256') -> bool:
        created_sign = ProdamusVerificate.create(data, key, algo)
        return created_sign and (created_sign.lower() == sign.lower())

    @staticmethod
    def _sort(data: Union[Dict, List]):
        if isinstance(data, dict):
            # Сортируем словарь по ключам
            sorted_data = sorted(data.items(), key=lambda x: str(x[0]))
            data.clear()
            for k, v in sorted_data:
                data[k] = v
                # Рекурсивно сортируем вложенные данные
                if isinstance(v, (dict, list)):
                    ProdamusVerificate._sort(v)
        elif isinstance(data, list):
            # Рекурсивно сортируем элементы списка
            for item in data:
                if isinstance(item, (dict, list)):
                    ProdamusVerificate._sort(item)