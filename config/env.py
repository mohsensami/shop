from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ARVAN CLOUD STORAGE
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = 'f3f68bd1-449a-43b9-8342-12f9c5ba3d2a'
AWS_SECRET_ACCESS_KEY = '60285a8f5fada0e085e578a0c9c3a01ac7eaaf5fd3ff2a8f098a842b25879c73'
AWS_S3_ENDPOINT_URL = 'https://s3.ir-thr-at1.arvanstorage.ir'
AWS_STORAGE_BUCKET_NAME = 'django-ecommerce'
AWS_SERVICE_NAME = 's3'
AWS_S3_FILE_OVERWRITE = False
AWS_LOCAL_STORAGE = f'{BASE_DIR}/aws/'

# zarrinpal
MERCHANT = '265a8793-1277-4f41-898e-3a49d1ca65a1'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"
CallbackURL = 'http://127.0.0.1:8000/orders/verify/'