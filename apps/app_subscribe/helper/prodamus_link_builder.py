from typing import MutableMapping, Any
from urllib.parse import urlencode

from domain.port.spi.payment.contract import PaymentLinkDTO
from domain.const.payment import PAYMENT_SYS
    

class PaymentLinkBuilder:
    def generate_payment_link(self, dto: PaymentLinkDTO) -> str:
        products: list[dict[str, Any]] = []
        for product in dto.products:
            products.append({
                'name': product.name,
                'price': product.price,
                'quantity': product.quantity
            })
        data = {
            "do": dto.do,
            "products": products,
            "sys": PAYMENT_SYS,
            "customer_email": dto.customer_email,
            "paid_content": dto.paid_content
        }
        data['signature'] = self.sign(data, dto.secret_key)
        link = dto.linktoform + '?' + urlencode(self.http_build_query(data))
        return link
        
    def sign(self, data, secret_key: str):
        import hashlib
        import hmac
        import json
        # переводим все значения data в string c помощью кастомной функции deep_int_to_string (см ниже)
        self.deep_int_to_string(data)
        # переводим data в JSON, с сортировкой ключей в алфавитном порядке, без пробелом и экранируем бэкслеши
        data_json = json.dumps(data, sort_keys=True, ensure_ascii=False, separators=(',', ':')).replace("/", "\\/")
        # создаем подпись с помощью библиотеки hmac и возвращаем ее
        return hmac.new(secret_key.encode('utf8'), data_json.encode('utf8'), hashlib.sha256).hexdigest()

    def deep_int_to_string(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(value, MutableMapping):
                self.deep_int_to_string(value)
            elif isinstance(value, list) or isinstance(value, tuple):
                for k, v in enumerate(value):
                    self.deep_int_to_string({str(k): v})
            else: dictionary[key] = str(value)

    def http_build_query(self, dictionary, parent_key=False):
        items = []
        for key, value in dictionary.items():
            new_key = str(parent_key) + '[' + key + ']' if parent_key else key
            if isinstance(value, MutableMapping):
                items.extend(self.http_build_query(value, new_key).items())
            elif isinstance(value, list) or isinstance(value, tuple):
                for k, v in enumerate(value):
                    items.extend(self.http_build_query({str(k): v}, new_key).items())
            else:
                items.append((new_key, value))
        return dict(items)