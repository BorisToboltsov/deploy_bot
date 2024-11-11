import os

import requests
from requests.auth import HTTPBasicAuth


class DbRequests:
    @staticmethod
    async def get(parameters: dict = None) -> requests:
        return requests.get(
            os.getenv("API_URL"),
            auth=HTTPBasicAuth(os.getenv("API_LOGIN"), os.getenv("API_PASSWORD")),
            params=parameters,
        ).json()
