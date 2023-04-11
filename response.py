from request import Request
from requestType import RequestType
class Response():
    def __init__(self,requestType,data):
        self.requestType = requestType
        self.data=data