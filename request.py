from requestType import RequestType

class Request():
    def __init__(self,type:RequestType,data):
        self.type = type
        self.data = data

    