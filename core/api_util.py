from core.rest_client import RestClient


class Api(RestClient):
    def __init__(self):
        super().__init__()

    def get_send_code(self, **kwargs):
        return self.post('/code/', **kwargs)

    def mobile_register(self, **kwargs):
        return self.post('/users/', **kwargs)

    def user_login(self, **kwargs):
        return self.post('/login/', **kwargs)

    def banners(self, **kwargs):
        return self.get('/banners/', **kwargs)

    def shopcarts(self, **kwargs):
        return self.post('/shopcarts/', **kwargs)

    def message(self, **kwargs):
        return self.post('/messages/', **kwargs)


api_util = Api()
