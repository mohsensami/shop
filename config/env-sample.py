from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ARVAN CLOUD STORAGE
DEFAULT_FILE_STORAGE = 'xxxxxxxxxxxxx'
AWS_ACCESS_KEY_ID = 'xxxxxxxxxxxxxx'
AWS_SECRET_ACCESS_KEY = 'xxxxxxxxxxxxxx'
AWS_S3_ENDPOINT_URL = 'xxxxxxxxxxxxxx'
AWS_STORAGE_BUCKET_NAME = 'xxxxxxxxxxxxxx'
AWS_SERVICE_NAME = 's3'
AWS_S3_FILE_OVERWRITE = False
AWS_LOCAL_STORAGE = f'{BASE_DIR}/aws/'

# zarrinpal
MERCHANT = 'xxxxxxxxxxxxxx'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"
CallbackURL = 'http://127.0.0.1:8000/orders/verify/'