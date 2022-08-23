import requests
import json
from . import exceptions

base_url = 'https://9anime.dev'

class client:
    def __init__():
        pass

    def search(self):
        r = requests.get(f'{base_url}/anime?search={self}')
        if r.status_code == 404:
            raise exceptions.NotFound('Not Found.')
        elif r.status_code != 200:
            raise Exception(r.content)
        return json.loads(json.dumps(r.json(), indent=4))

__version__ = '1.0.0'