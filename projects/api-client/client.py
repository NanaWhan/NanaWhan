import json
from urllib.request import urlopen, Request
from urllib.parse import urlencode

class APIClient:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url.rstrip("/")
        self.headers = headers or {"Content-Type": "application/json"}
    
    def _request(self, method, path, data=None, params=None):
        url = f"{self.base_url}/{path.lstrip('/')}"
        if params:
            url += "?" + urlencode(params)
        body = json.dumps(data).encode() if data else None
        req = Request(url, data=body, headers=self.headers, method=method)
        with urlopen(req) as resp:
            return json.loads(resp.read().decode())
    
    def get(self, path, params=None):
        return self._request("GET", path, params=params)
    
    def post(self, path, data):
        return self._request("POST", path, data=data)
    
    def put(self, path, data):
        return self._request("PUT", path, data=data)
    
    def delete(self, path):
        return self._request("DELETE", path)

if __name__ == "__main__":
    client = APIClient("https://jsonplaceholder.typicode.com")
    posts = client.get("/posts", params={"_limit": 5})
    for p in posts:
        print(f"  [{p['id']}] {p['title']}")
