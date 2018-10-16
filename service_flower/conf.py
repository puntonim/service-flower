# -*- coding: utf-8 -*-
from pkgsettings import Settings

settings = Settings()
settings.configure(
    BASE_URL='localhost/api',
    REQUEST_TIMEOUT=30,
    HTTP_AUTH_USERNAME='user',
    HTTP_AUTH_PASSWORD='pass',
)
