# Import
from adfly import AdflyApi


def short(url):
    api = AdflyApi(
        user_id=14525055,
        public_key='',
        secret_key='',
    )
    return api.shorten(url)
