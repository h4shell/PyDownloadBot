# Import
from adfly import AdflyApi


def short(url):
    api = AdflyApi(
        user_id=,
        public_key='',
        secret_key='',
    )
    return api.shorten(url)
