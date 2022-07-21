from client import APIClient

class AuthenticatedClient(APIClient):
    def __init__(self, base_url, token=None, api_key=None):
        headers = {"Content-Type": "application/json"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        if api_key:
            headers["X-API-Key"] = api_key
        super().__init__(base_url, headers)
    
    def set_token(self, token):
        self.headers["Authorization"] = f"Bearer {token}"
    
    def login(self, username, password):
        response = self.post("/auth/login", {"username": username, "password": password})
        if "token" in response:
            self.set_token(response["token"])
        return response

class RateLimitedClient(AuthenticatedClient):
    def __init__(self, base_url, max_requests=60, **kwargs):
        super().__init__(base_url, **kwargs)
        self.max_requests = max_requests
        self.request_count = 0
    
    def _request(self, method, path, **kwargs):
        self.request_count += 1
        if self.request_count > self.max_requests:
            raise Exception("Rate limit exceeded")
        return super()._request(method, path, **kwargs)
