import os
import hashlib
import urllib.parse

ROBOKASSA_LOGIN = os.getenv("ROBOKASSA_LOGIN")
ROBOKASSA_PASSWORD1 = os.getenv("ROBOKASSA_PASSWORD1")
ROBOKASSA_PASSWORD2 = os.getenv("ROBOKASSA_PASSWORD2")
ROBOKASSA_URL = "https://auth.robokassa.ru/Merchant/Index.aspx"

def create_payment_link(user_id: int, amount: float = 10.0):
    invoice_id = user_id
    description = f"Подписка на Trend→Money AI"
    signature = hashlib.md5(f"{ROBOKASSA_LOGIN}:{amount}:{invoice_id}:{ROBOKASSA_PASSWORD1}".encode()).hexdigest()
    params = {
        "MrchLogin": ROBOKASSA_LOGIN,
        "OutSum": amount,
        "InvId": invoice_id,
        "Desc": description,
        "SignatureValue": signature,
        "IsTest": 1  # 0 для реальных платежей
    }
    return f"{ROBOKASSA_URL}?{urllib.parse.urlencode(params)}"